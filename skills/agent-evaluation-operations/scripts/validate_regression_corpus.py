#!/usr/bin/env python3
"""Validate the bundled behavioral regression corpus without external packages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


REQUIRED_LIST_FIELDS = (
    "allowed_resources",
    "expected_behaviors",
    "prohibited_behaviors",
    "evidence",
    "failure_evidence",
    "side_effects_allowed",
    "applicable_skills",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "corpus",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "references" / "regression-corpus.json",
    )
    parser.add_argument("--expected-count", type=int, default=None)
    args = parser.parse_args()

    try:
        data = json.loads(args.corpus.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("corpus root must be an object")
    except (OSError, ValueError) as exc:
        print(f"ERROR: invalid corpus: {exc}", file=sys.stderr)
        return 2
    expected = args.expected_count if args.expected_count is not None else data.get("expected_case_count")
    if data.get("schema_version") != "1.1":
        errors = ["schema_version must be 1.1"]
    else:
        errors = []
    scorer_contracts = data.get("scorer_contracts")
    if not isinstance(scorer_contracts, dict) or not scorer_contracts:
        errors.append("scorer_contracts must be a non-empty object")
        scorer_contracts = {}
    for name, contract in scorer_contracts.items():
        if not isinstance(name, str) or not name.strip() or not isinstance(contract, dict):
            errors.append("each scorer contract needs a name and object")
            continue
        for field in ("deterministic_checks", "rubric_checks", "critical_failure"):
            value = contract.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"scorer {name}: {field} must be a non-empty string")
    cases = data.get("cases")
    if not isinstance(cases, list):
        errors.append("top-level cases must be a list")
        cases = []
    if type(expected) is not int or expected < 1:
        errors.append("positive expected_case_count or --expected-count is required")
    elif len(cases) != expected:
        errors.append(f"expected {expected} cases, found {len(cases)}")

    seen: set[str] = set()
    for index, case in enumerate(cases, start=1):
        prefix = f"case {index}"
        if not isinstance(case, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{prefix}: missing id")
        elif case_id in seen:
            errors.append(f"{prefix}: duplicate id {case_id}")
        else:
            seen.add(case_id)
        for field in ("title", "category", "prompt"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"{prefix}: {field} must be a non-empty string")
        if not isinstance(case.get("scorer"), str) or not case["scorer"].strip():
            errors.append(f"{prefix}: scorer must be a non-empty string")
        elif case["scorer"] not in scorer_contracts:
            errors.append(f"{prefix}: scorer has no matching scorer_contract")
        threshold = case.get("acceptance_threshold")
        if not isinstance(threshold, dict):
            errors.append(f"{prefix}: acceptance_threshold must be an object")
        else:
            if threshold.get("required_behaviors") != "all":
                errors.append(f"{prefix}: required_behaviors must be all")
            if threshold.get("required_evidence") != "all":
                errors.append(f"{prefix}: required_evidence must be all")
            if type(threshold.get("prohibited_behaviors_allowed")) is not int or threshold["prohibited_behaviors_allowed"] != 0:
                errors.append(f"{prefix}: prohibited_behaviors_allowed must be 0")
        for field in REQUIRED_LIST_FIELDS:
            value = case.get(field)
            if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
                errors.append(f"{prefix}: {field} must be a non-empty string list")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS structure only: {len(cases)} unique regression cases in {args.corpus}; no model behavior executed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
