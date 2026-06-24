# Public Release Checklist

Use this checklist to verify the repository before a public release.

## Required Checks

- Confirm `skills/` contains exactly 70 public-core skill folders.
- Confirm `manifest.json` reports `"skill_count": 70`.
- Confirm `SKILL_INVENTORY.md` reports `Total skills: 70`.
- Run `python3 scripts/validate_skills.py`.
- Run `python3 scripts/install_skills.py --list-collections`.
- Run `python3 scripts/install_skills.py --dry-run` and confirm it installs `public-core` only.
- Run `python3 -m py_compile scripts/install_skills.py scripts/generate_inventory.py scripts/validate_skills.py`.
- Run `git diff --check`.
- Review `skills/` for private paths, secrets, credentials, private links, client-specific material, and bundled assets that require attribution.
- Confirm `README.md` presents the project clearly and does not promise guaranteed output quality.
- Confirm `SECURITY.md` documents installer behavior and replacement backups.
- Confirm `SKILL_QUALITY_STANDARD.md` defines contribution criteria.
- Confirm `CURATED_COLLECTIONS.md` and `curated_collections.json` define `public-core` as the default public release.
- Confirm `THIRD_PARTY_NOTICES.md` describes notice expectations and excluded integrations.

## Showcase Checks

- Confirm `examples/premium-website-showcase/gallery/index.html` opens locally.
- Confirm all gallery preview links point to checked-in demo files.
- Confirm there are 9 checked-in demo preview files:

```bash
find examples/premium-website-showcase/demos -name "preview.html" | wc -l
```

- Confirm there are 9 checked-in demo ZIP files:

```bash
ls examples/premium-website-showcase/demo-zips | wc -l
```

## Recommended Polish

- Add at least one measured benchmark under `examples/benchmarks/`.
- Add screenshots or screen recordings for the showcase or benchmark examples.
- Add GitHub repository topics such as `codex`, `codex-skills`, `frontend`, `web-design`, `nextjs`, `accessibility`, and `webgl`.
- Publish from a clean repository state with no private/local export history exposed.
