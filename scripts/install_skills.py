#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install shared Codex skills.")
    parser.add_argument("--source", default=str(Path(__file__).resolve().parents[1] / "skills"))
    parser.add_argument("--dest", default=str(Path.home() / ".codex" / "skills"))
    parser.add_argument(
        "--collection",
        action="append",
        default=[],
        help="Install one curated public-core collection from curated_collections.json. May be passed more than once.",
    )
    parser.add_argument("--list-collections", action="store_true", help="List curated collections and exit.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without copying files.")
    parser.add_argument("--replace", action="store_true", help="Replace existing skills with backups.")
    return parser.parse_args()


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and (path / "SKILL.md").exists()


def load_collection_data(repo_root: Path) -> dict[str, object]:
    path = repo_root / "curated_collections.json"
    if not path.exists():
        return {"collections": []}
    return json.loads(path.read_text(encoding="utf-8"))


def collection_map(data: dict[str, object]) -> dict[str, dict[str, object]]:
    return {collection["id"]: collection for collection in data.get("collections", [])}


def requested_collections(args: argparse.Namespace, data: dict[str, object]) -> list[str]:
    if args.collection:
        return args.collection
    default = data.get("default_collection")
    return [str(default)] if default else []


def select_skills(skills: list[Path], collections: dict[str, dict[str, object]], requested: list[str]) -> list[Path]:
    if not requested:
        return skills
    by_name = {skill.name: skill for skill in skills}
    selected_names: set[str] = set()
    missing_collections = [name for name in requested if name not in collections]
    if missing_collections:
        raise SystemExit(f"Unknown collection(s): {', '.join(sorted(missing_collections))}")
    for collection_id in requested:
        for skill_name in collections[collection_id].get("skills", []):
            if skill_name not in by_name:
                raise SystemExit(f"Collection {collection_id} references missing skill: {skill_name}")
            selected_names.add(skill_name)
    return [skill for skill in skills if skill.name in selected_names]


def copy_skill(src: Path, dest: Path, dry_run: bool, replace: bool, backups: Path) -> str:
    target = dest / src.name
    if target.exists() and not replace:
        return "skipped"
    if dry_run:
        return "would_replace" if target.exists() else "would_install"
    if target.exists():
        backups.mkdir(parents=True, exist_ok=True)
        backup = backups / src.name
        if backup.exists():
            shutil.rmtree(backup)
        shutil.move(str(target), str(backup))
    shutil.copytree(
        src,
        target,
        ignore=shutil.ignore_patterns("__pycache__", ".DS_Store", "*.pyc"),
    )
    return "replaced" if (backups / src.name).exists() else "installed"


def main() -> None:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    dest = Path(args.dest).expanduser().resolve()
    repo_root = Path(__file__).resolve().parents[1]
    data = load_collection_data(repo_root)
    collections = collection_map(data)
    requested = requested_collections(args, data)

    if args.list_collections:
        if not collections:
            print("No curated collections found.")
            return
        default = data.get("default_collection")
        for collection in collections.values():
            skill_count = len(collection.get("skills", []))
            suffix = " [default]" if collection.get("id") == default else ""
            print(f"{collection['id']}: {collection.get('title', '')} ({skill_count} skills){suffix}")
        return

    if not source.exists():
        raise SystemExit(f"Missing source skills directory: {source}")
    skills = sorted([p for p in source.iterdir() if is_skill_dir(p)], key=lambda p: p.name)
    skills = select_skills(skills, collections, requested)
    if not skills:
        raise SystemExit(f"No matching skill folders found in {source}")

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backups = dest / f".backup-before-shared-skills-{stamp}"
    counts: dict[str, int] = {}
    if not args.dry_run:
        dest.mkdir(parents=True, exist_ok=True)
    for skill in skills:
        result = copy_skill(skill, dest, args.dry_run, args.replace, backups)
        counts[result] = counts.get(result, 0) + 1

    print(f"source={source}")
    print(f"dest={dest}")
    if requested:
        print(f"collections={','.join(requested)}")
    print(f"skills={len(skills)}")
    for key in sorted(counts):
        print(f"{key}={counts[key]}")
    if args.replace and not args.dry_run:
        print(f"backups={backups}")
    print("Start a new Codex conversation after install so skills are rediscovered.")


if __name__ == "__main__":
    main()
