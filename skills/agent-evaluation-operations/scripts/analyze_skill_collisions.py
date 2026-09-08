#!/usr/bin/env python3
"""Rank possible Codex skill-description collisions for semantic review."""

from __future__ import annotations

import argparse
import itertools
import json
import math
import os
import sys
from pathlib import Path
import re


STOP = {
    "a", "an", "and", "any", "as", "at", "be", "before", "build", "create",
    "design", "do", "for", "from", "in", "into", "is", "it", "of", "on",
    "or", "the", "this", "to", "use", "uses", "using", "when", "with",
    "work", "workflow", "website", "websites", "app", "apps", "skill",
}


def frontmatter_value(text: str, key: str) -> str:
    """Read common scalar frontmatter forms; unsupported metadata is unassessed."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return ""
    hits = [(i, line[len(key) + 1:].strip()) for i, line in enumerate(lines[1:end], 1) if line.startswith(key + ":")]
    if len(hits) != 1:
        return ""
    index, value = hits[0]
    if re.fullmatch(r"[>|][+-]?", value):
        parts = []
        for line in lines[index + 1:end]:
            if line and not line[0].isspace():
                break
            parts.append(line.strip())
        return " ".join(parts).strip()
    if value.startswith('"'):
        try:
            decoded, stop = json.JSONDecoder().raw_decode(value)
            tail = value[stop:].strip()
            return decoded if isinstance(decoded, str) and (not tail or tail.startswith("#")) else ""
        except ValueError:
            return ""
    if value.startswith("'"):
        match = re.fullmatch(r"'((?:[^']|'')*)'\s*(?:#.*)?", value)
        return match.group(1).replace("''", "'") if match else ""
    value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
    if not value or value[0] in "[{&*!" or value.lower() in {"null", "~", "true", "false"}:
        return ""
    return value


def tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", value.lower())
        if len(token) > 2 and token not in STOP
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").expanduser() / "skills")
    parser.add_argument("--threshold", type=float, default=0.42)
    parser.add_argument("--limit", type=int, default=80)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if not args.root.is_dir() or args.root.is_symlink():
        parser.error("--root must be an existing regular skill directory")
    if not math.isfinite(args.threshold) or not 0 <= args.threshold <= 1 or args.limit < 1:
        parser.error("--threshold must be 0-1 and --limit must be positive")
    skills = []
    skipped = []
    for path in sorted(args.root.glob("*/SKILL.md")):
        if path.parent.is_symlink() or path.is_symlink():
            skipped.append(path.parent.name)
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            skipped.append(path.parent.name)
            continue
        name = frontmatter_value(text, "name") or path.parent.name
        description = frontmatter_value(text, "description")
        if not description:
            skipped.append(path.parent.name)
            continue
        word_set = tokens(f"{name} {description}")
        if word_set:
            skills.append({"name": name, "description": description, "tokens": word_set})

    pairs = []
    for left, right in itertools.combinations(skills, 2):
        shared = left["tokens"] & right["tokens"]
        if len(shared) < 2:
            continue
        union = left["tokens"] | right["tokens"]
        jaccard = len(shared) / len(union)
        containment = len(shared) / min(len(left["tokens"]), len(right["tokens"]))
        score = max(jaccard, containment * 0.85)
        if score >= args.threshold:
            pairs.append({
                "left": left["name"],
                "right": right["name"],
                "score": round(score, 3),
                "shared": sorted(shared),
            })
    pairs.sort(key=lambda item: (-item["score"], item["left"], item["right"]))
    pairs = pairs[: args.limit]

    if args.json:
        print(json.dumps({"root": str(args.root), "assessed_skills": len(skills), "unassessed": skipped, "pairs": pairs, "scope": "lexical candidates only; semantic review required"}, indent=2))
    else:
        print("score\tleft\tright\tshared_terms")
        for pair in pairs:
            print(f"{pair['score']:.3f}\t{pair['left']}\t{pair['right']}\t{','.join(pair['shared'])}")
        print(f"CANDIDATES: {len(pairs)} (lexical discovery only; semantic review required)")
    if skipped:
        print(f"UNASSESSED: {len(skipped)} unreadable, symlinked or unsupported descriptions", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
