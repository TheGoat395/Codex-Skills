#!/usr/bin/env python3
"""Check public skill portability; not a universal privacy/security certificate."""
from pathlib import Path
import json
import os
import re
import sys
from generate_inventory import skill_info

ROOT = Path(__file__).resolve().parents[1]
HOME_PATH = re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\Users\\)([A-Za-z0-9_.-]+)")
EXAMPLE_USERS = {"user", "username", "example"}
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")


def inspect(root: Path) -> list[str]:
    errors = []
    skills = root / "skills"
    if skills.is_symlink() or not skills.is_dir():
        return ["skills/: missing directory or symbolic-link root"]
    for current, dirs, files in os.walk(skills, followlinks=False):
        for name in dirs + files:
            p = Path(current) / name
            if p.is_symlink():
                errors.append(f"{p.relative_to(root)}: symbolic link is not portable")
        dirs[:] = [d for d in dirs if not (Path(current) / d).is_symlink() and d != "__pycache__"]
        for name in files:
            p = Path(current) / name
            if p.is_symlink() or p.suffix in {".pyc", ".pyo"}:
                continue
            try:
                text = p.read_text(encoding="utf-8")
            except UnicodeError:
                continue
            if any(m.group(1).lower() not in EXAMPLE_USERS for m in HOME_PATH.finditer(text)):
                errors.append(f"{p.relative_to(root)}: machine-specific home path")
            if p.suffix != ".md":
                continue
            for target in LINK.findall(text):
                target = target.split("#", 1)[0]
                if not target or target.startswith(("https:", "http:", "mailto:", "/", "~")) or any(c in target for c in "<>*` "):
                    continue
                resolved = Path(os.path.abspath(p.parent / target))
                if not resolved.is_relative_to(root.absolute()):
                    errors.append(f"{p.relative_to(root)}: local reference escapes package")
                    continue
                if any(parent.is_symlink() for parent in (resolved, *resolved.parents) if parent.is_relative_to(root.absolute())):
                    errors.append(f"{p.relative_to(root)}: local reference traverses symbolic link")
                    continue
                if not resolved.exists():
                    errors.append(f"{p.relative_to(root)}: missing local reference {target}")
    # Do not traverse symlinks while computing the inventory.
    if errors:
        return errors
    manifest = root / "manifest.json"
    if manifest.is_symlink() or not manifest.is_file():
        return ["manifest.json: missing regular inventory file or symbolic link"]
    try:
        data = json.loads(manifest.read_text())
    except (OSError, ValueError):
        return ["manifest.json: unreadable or invalid JSON"]
    actual = [skill_info(p) for p in sorted(skills.iterdir()) if p.is_dir() and (p / "SKILL.md").is_file()]
    if not isinstance(data, dict) or data.get("skills") != actual or data.get("skill_count") != len(actual):
        errors.append("manifest.json: inventory differs from packaged source; regenerate it")
    return errors


def main() -> int:
    errors = inspect(ROOT)
    for error in errors:
        print("ERROR: " + error, file=sys.stderr)
    if errors:
        return 1
    print("Public package: local references, home-path screening, symlinks and inventory passed")
    print("This does not scan all personal data, external URLs or model behavior; review content and run a secret scanner separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
