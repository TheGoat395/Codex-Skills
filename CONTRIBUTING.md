# Contributing

Contributions should make this skill pack more useful, safer, or easier to evaluate.

## Good Contributions

- new skills that fill a clear workflow gap
- tighter skill descriptions and trigger boundaries
- benchmark examples
- installer safety improvements
- collection curation
- docs that help users install selectively and evaluate results honestly

## Before Opening A Pull Request

Run:

```bash
python3 scripts/validate_skills.py
python3 scripts/generate_inventory.py
git diff --check
```

If you change skill folders, regenerate `manifest.json` and `SKILL_INVENTORY.md`.

## Skill Naming

Use lowercase kebab-case names:

```text
frontend-example-skill
```

Avoid vague names like:

```text
better-design
awesome-sites
```

## Pull Request Checklist

- The change has a clear user-facing purpose.
- New or changed skills meet `SKILL_QUALITY_STANDARD.md`.
- Collections are updated when relevant.
- Generated inventory files are refreshed.
- No private paths, secrets, credentials, or personal-only instructions are included.
- Verification commands are reported honestly.
