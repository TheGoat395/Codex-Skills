# Maintainer Workflow

This repository is an unofficial community project. It is not an official OpenAI project and is not endorsed by OpenAI.

The maintainer workflow is designed to keep the public skill library inspectable, installable, and easy to evaluate.

## Standard Maintenance Loop

1. Inspect the requested change and identify whether it affects skills, collections, docs, installer behavior, examples, or generated inventory.
2. Keep changes scoped to the public use case.
3. Avoid private paths, account-specific instructions, credentials, secrets, and non-public assets.
4. Validate skill structure before release.
5. Regenerate inventory when skill folders or metadata change.
6. Record evidence through examples, benchmark templates, or measured benchmarks.
7. Push only after validation passes.

## Validation Commands

Run these before releasing changes:

```bash
python3 scripts/validate_skills.py
python3 scripts/generate_inventory.py
git diff --check
```

If generated files change, include `manifest.json` and `SKILL_INVENTORY.md` in the same commit.

## Release Checklist

- [ ] `README.md` reflects the current install path and positioning.
- [ ] `INSTALL.md` works for clone-based and release-archive installs.
- [ ] `curated_collections.json` points only to existing skills.
- [ ] `manifest.json` and `SKILL_INVENTORY.md` are current.
- [ ] `scripts/validate_skills.py` passes.
- [ ] `git diff --check` passes.
- [ ] Release archive does not include private assets, `skills.zip`, `__MACOSX`, `.DS_Store`, or local-only files.
- [ ] Changelog entry describes user-facing changes.
- [ ] GitHub Actions validation is green on `main`.

## Evidence Policy

Use three evidence levels:

| Evidence Level | Meaning |
|---|---|
| Proof-of-output showcase | Checked-in local artifacts that demonstrate the type of output the workflow can produce. |
| Workflow impact estimate | A reasoned estimate based on skill coverage, expected failure modes, and evaluation criteria. |
| Measured benchmark | A controlled baseline-vs-skill-assisted comparison with saved outputs and verification notes. |

Do not present workflow estimates as measured benchmark results. Keep measured claims tied to saved evidence.
