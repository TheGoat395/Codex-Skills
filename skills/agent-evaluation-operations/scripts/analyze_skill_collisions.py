#!/usr/bin/env python3
"""Rank possible Codex skill-description collisions for semantic review."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import re


STOP = {
    "a", "an", "and", "any", "as", "at", "be", "before", "build", "create",
    "design", "do", "for", "from", "in", "into", "is", "it", "of", "on",
    "or", "the", "this", "to", "use", "uses", "using", "when", "with",
    "work", "workflow", "website", "websites", "app", "apps", "skill",
}


def frontmatter_value(text: str, key: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end < 0:
        return ""
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text[3:end])
    if not match:
        return ""
    return match.group(1).strip().strip('"\'')


def tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", value.lower())
        if len(token) > 2 and token not in STOP
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.home() / ".codex" / "skills")
    parser.add_argument("--threshold", type=float, default=0.42)
    parser.add_argument("--limit", type=int, default=80)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    skills = []
    for path in sorted(args.root.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        name = frontmatter_value(text, "name") or path.parent.name
        description = frontmatter_value(text, "description")
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
        print(json.dumps({"root": str(args.root), "pairs": pairs}, indent=2))
    else:
        print("score\tleft\tright\tshared_terms")
        for pair in pairs:
            print(f"{pair['score']:.3f}\t{pair['left']}\t{pair['right']}\t{','.join(pair['shared'])}")
        print(f"CANDIDATES: {len(pairs)} (lexical discovery only; semantic review required)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
