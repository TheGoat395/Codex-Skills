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
        # Only root fields control the skill; nested UI metadata must not override them.
        if not line or line[0].isspace() or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key not in {"name", "description"}:
            continue
        if key in data:
            return {}  # Ambiguous required metadata is not a valid catalog entry.
        if value in {">", ">-", "|", "|-"}:
            block = []
            for follow in lines[index + 1:]:
                if follow and not follow[0].isspace():
                    break
                block.append(follow.strip())
            value = " ".join(part for part in block if part)
        elif value.startswith('"'):
            try:
                decoded, end = json.JSONDecoder().raw_decode(value)
                remainder = value[end:].strip()
                if remainder and not remainder.startswith("#"):
                    return {}
                value = decoded
            except ValueError:
                return {}
        elif value.startswith("'"):
            match = re.fullmatch(r"'((?:[^']|'')*)'\s*(?:#.*)?", value)
            if not match:
                return {}
            value = match.group(1).replace("''", "'")
        else:
            value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
            if value.lower() in {"null", "~", "true", "false"} or re.fullmatch(r"[-+]?\d+(?:\.\d+)?", value) or value.startswith(("[", "{", "*", "&", "!")):
                return {}
        if not isinstance(value, str):
            return {}
        data[key] = value
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
        if not description.strip():
            errors.append(f"{skill_dir}: description is missing or blank")

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
