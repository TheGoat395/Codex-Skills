# Maintainers

Codex Premium Website Skills is maintained as an unofficial open-source community skill library.

## Project Stewardship

The project owner is responsible for:

- keeping the public core curated
- reviewing contribution safety and scope
- validating skill metadata and inventory
- keeping install instructions accurate
- maintaining benchmark and proof-of-output documentation
- keeping unofficial OpenAI/Codex positioning clear

## Review Priorities

Public changes should improve at least one of these areas:

- practical usefulness for Codex users
- installation safety
- skill clarity and trigger boundaries
- benchmark evidence
- showcase quality
- documentation accuracy
- maintainer workflow reliability

## Release Validation

Before a public release:

```bash
python3 scripts/validate_skills.py
python3 scripts/generate_inventory.py
git diff --check
```

If skills or collections changed, include refreshed generated inventory files in the release commit.

## Contact

Use GitHub issues for bug reports, skill requests, showcase submissions, and documentation corrections.
