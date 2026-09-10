# Repository Operating Notes

Codex-Skills is a public, Codex-first Agent Skills library. Keep the public core curated, installable, inspectable, and honest about evidence.

## Required Checks

Before a release or pull request that changes skills, collections, scripts, docs, or workflows, run:

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_public_package.py
python3 scripts/test_catalog.py
python3 scripts/test_skill_helpers.py
python3 scripts/install_skills.py --list-collections
python3 scripts/install_skills.py --dry-run
python3 -m py_compile scripts/*.py
git diff --check
```

Regenerate `manifest.json` and `SKILL_INVENTORY.md` when skill folders change.

## Evidence Rules

- Label measured results, estimates, owner-only GitHub metrics, and derived calculations separately.
- Never invent users, forks, issues, benchmark results, testimonials, or adoption claims.
- Preserve the exact prompt, outputs, commands, and limitations for paired benchmarks.
- Do not present fictional values inside a demo mockup as repository telemetry.
- Treat browser, accessibility, performance, and security checks as unperformed until they actually run.

## Change Hygiene

- Inspect the worktree before editing and use a branch for risky changes.
- Keep installer behavior explicit and preserve dry-run and backup-on-replace safeguards.
- Do not add secrets, private paths, credentials, generated caches, or machine-specific state.
- Before public commits, verify the repository author/committer identity is suitable for publication; do not rely on an automatically inferred machine address.
- Prefer focused changes that improve usefulness, safety, reproducibility, or documentation.
