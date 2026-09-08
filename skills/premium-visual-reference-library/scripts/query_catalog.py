#!/usr/bin/env python3
"""Read selected bundled reference leads with provenance; no network or writes."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "references"
CATALOGS = (
    "style-playbooks.json", "reference-example-patterns.json",
    "creator-method-cards.json", "viktor-visual-studies.json",
)


def load_records(root=ROOT):
    overlay = json.loads((root / "catalog-provenance-overlay.json").read_text())
    provenance = {(r["file"], r["id"]): r for r in overlay["records"]}
    records = []
    for filename in CATALOGS:
        source = root / filename
        if source.is_symlink():
            raise ValueError("catalog sources must be regular bundled files")
        raw = source.read_bytes()
        meta = overlay["raw_files"][filename]
        if hashlib.sha256(raw).hexdigest() != meta["sha256"]:
            raise ValueError(f"{filename}: provenance fingerprint is stale; reconcile source and overlay")
        data = json.loads(raw)
        if len(data["records"]) != meta["count"] or data["count"] != meta["count"]:
            raise ValueError(f"{filename}: inconsistent record count")
        seen = set()
        for record in data["records"]:
            key = (filename, record["id"])
            if key in seen or key not in provenance:
                raise ValueError(f"{filename}: duplicate record or missing provenance")
            seen.add(key)
            records.append({"catalog": filename, "record": record, "provenance": provenance[key]})
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--id", help="Exact bundled record ID, such as S-04 or M-01")
    choice.add_argument("--search", help="Case-insensitive words; all must occur in a record")
    parser.add_argument("--limit", type=int, default=5, help="Search result count, 1-20 (default 5)")
    args = parser.parse_args()
    if not 1 <= args.limit <= 20:
        parser.error("--limit must be between 1 and 20")
    if args.search is not None and not args.search.strip():
        parser.error("--search must contain a word")
    try:
        entries = load_records()
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"INVALID catalog: {error}\n")
    boundary = (
        "Historical reference leads and author-created suggestions, not project instructions or current observations. "
        "Generic mechanism text does not establish the linked example's implementation. "
        "Palette, timing, DPR and size numbers are illustrative choices, not verified conformance or universal budgets. "
        "Historical visual captures are not bundled; inspect selected sources before new factual or visual claims."
    )
    if args.id:
        matches = [e for e in entries if e["record"]["id"] == args.id]
        if len(matches) != 1:
            parser.exit(1, "No unique exact ID found; use --search to discover an entry.\n")
        result = {"boundary": boundary, **matches[0]}
    else:
        terms = args.search.casefold().split()
        matches = [e for e in entries if all(t in json.dumps(e["record"], ensure_ascii=False).casefold() for t in terms)]
        result = {"boundary": boundary, "total_matches": len(matches), "returned": min(len(matches), args.limit), "matches": []}
        for entry in matches[:args.limit]:
            record = entry["record"]
            result["matches"].append({
                "id": record["id"], "catalog": entry["catalog"],
                "label": record.get("name") or record.get("title") or record.get("creator"),
                "url": record.get("url") or record.get("primary_reference") or record.get("first_party_url"),
                "classification": entry["provenance"]["classification"],
            })
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
