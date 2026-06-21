#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MANIFEST = ROOT / "manifest.json"
INVENTORY = ROOT / "SKILL_INVENTORY.md"


def read_description(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return ""
    frontmatter = match.group(1)
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("description:"):
            continue
        value = line.split(":", 1)[1].strip()
        if value in {">", ">-", "|", "|-"}:
            block: list[str] = []
            for follow in lines[index + 1 :]:
                if follow and not follow.startswith(" "):
                    break
                block.append(follow.strip())
            return " ".join(part for part in block if part)
        return value.strip('"')
    return ""


def skill_info(path: Path) -> dict[str, object]:
    files = [p for p in path.rglob("*") if p.is_file()]
    return {
        "name": path.name,
        "description": read_description(path / "SKILL.md"),
        "file_count": len(files),
        "bytes": sum(p.stat().st_size for p in files),
    }


def build_manifest(skills: list[dict[str, object]]) -> dict[str, object]:
    return {
        "name": "codex-premium-website-skills",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "skills/",
        "skill_count": len(skills),
        "skills": skills,
        "notes": [
            "Skill folders are packaged under skills/.",
            "Repo-level README, installer, inventory, collections, and standards files are packaging support.",
            "Install to ~/.codex/skills, then start a new Codex conversation to refresh discovery.",
        ],
    }


def inventory_markdown(skills: list[dict[str, object]]) -> str:
    lines = [
        "# Skill Inventory",
        "",
        f"Total skills: `{len(skills)}`",
        "",
        "Generated from `skills/*/SKILL.md`.",
        "",
        "| Skill | Description | Files | Size |",
        "|---|---|---:|---:|",
    ]
    for skill in skills:
        description = str(skill["description"]).replace("|", "\\|")
        lines.append(
            f"| `{skill['name']}` | {description} | {skill['file_count']} | {skill['bytes']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    skill_dirs = sorted(
        [p for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").exists()],
        key=lambda p: p.name,
    )
    skills = [skill_info(path) for path in skill_dirs]
    MANIFEST.write_text(json.dumps(build_manifest(skills), indent=2) + "\n", encoding="utf-8")
    INVENTORY.write_text(inventory_markdown(skills), encoding="utf-8")
    print(f"generated {len(skills)} skills")
    print(MANIFEST)
    print(INVENTORY)


if __name__ == "__main__":
    main()
