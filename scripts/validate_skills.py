#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
COLLECTIONS = ROOT / "curated_collections.json"


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    lines = match.group(1).splitlines()
    for index, line in enumerate(lines):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value in {">", ">-", "|", "|-"}:
                block: list[str] = []
                for follow in lines[index + 1 :]:
                    if follow and not follow.startswith(" "):
                        break
                    block.append(follow.strip())
                data[key] = " ".join(part for part in block if part)
            else:
                data[key] = value.strip('"')
    return data


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(
        [p for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").exists()],
        key=lambda p: p.name,
    )
    skill_names = {p.name for p in skill_dirs}

    for skill_dir in skill_dirs:
        metadata = parse_frontmatter(skill_dir / "SKILL.md")
        if metadata.get("name") != skill_dir.name:
            errors.append(f"{skill_dir}: frontmatter name does not match folder name")
        description = metadata.get("description", "")
        if len(description) < 40:
            errors.append(f"{skill_dir}: description is missing or too short")

    if COLLECTIONS.exists():
        data = json.loads(COLLECTIONS.read_text(encoding="utf-8"))
        seen_ids: set[str] = set()
        for collection in data.get("collections", []):
            collection_id = collection.get("id", "")
            if not collection_id:
                errors.append("collection missing id")
            if collection_id in seen_ids:
                errors.append(f"duplicate collection id: {collection_id}")
            seen_ids.add(collection_id)
            for name in collection.get("skills", []):
                if name not in skill_names:
                    errors.append(f"collection {collection_id} references missing skill: {name}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"validated {len(skill_dirs)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
