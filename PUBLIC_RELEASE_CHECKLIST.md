# Public Release Checklist

Use this checklist before changing any release repository from private to public.

## Required

- Confirm `skills/` contains exactly 70 public-core skill folders.
- Confirm `manifest.json` says `"skill_count": 70`.
- Confirm `SKILL_INVENTORY.md` says `Total skills: `70``.
- Run `python3 scripts/validate_skills.py`.
- Run `python3 scripts/install_skills.py --list-collections`.
- Run `python3 scripts/install_skills.py --dry-run` and confirm it installs `public-core` only.
- Run `python3 -m py_compile scripts/install_skills.py scripts/generate_inventory.py scripts/validate_skills.py`.
- Run `git diff --check`.
- Review `skills/` for private paths, secrets, credentials, private links, client-specific material, and bundled assets that require attribution.
- Confirm `README.md` says this is unofficial and does not guarantee better output.
- Confirm `SECURITY.md` documents installer behavior and replacement backups.
- Confirm `SKILL_QUALITY_STANDARD.md` defines contribution criteria.
- Confirm `CURATED_COLLECTIONS.md` and `curated_collections.json` define `public-core` as the default 70-skill public release.
- Confirm `THIRD_PARTY_NOTICES.md` does not claim excluded/private integrations are bundled in the public release.

## Strongly Recommended

- Add at least one real benchmark under `examples/`.
- Add screenshots or links for before/after frontend examples.
- Add GitHub repository topics such as `codex`, `codex-skills`, `frontend`, `web-design`, `nextjs`, `accessibility`, and `webgl`.
- Publish from a fresh clean repository or a history-rewritten release repository so old private/local export history is not exposed.

## OpenAI Codex For Open Source Positioning

Use honest maintainer language:

> I maintain an open-source Codex skill library for premium frontend and website workflows. The project packages repeatable Codex workflows for design quality, frontend implementation, motion, accessibility, performance QA, QA discipline, content polish, and production handoff.

Avoid entitlement language. The project should be presented as a useful ecosystem contribution, not as a request for benefits because the skill count is high.
