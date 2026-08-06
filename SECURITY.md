# Security Policy

This repository contains Codex skill instructions and installer scripts. Treat both as code-adjacent material. Inspect before running.

## Supported Use

Use this repo only on machines and repositories where you have permission to install skills and run Codex workflows.

Do not use these skills or any related tooling to scan, modify, probe, or review systems you do not own or are not authorized to work on.

## Installer Behavior

`scripts/install_skills.py` copies skill folders from this repo into `~/.codex/skills`.

Default behavior:

- copies only missing skills
- skips existing skills
- does not install Python packages
- does not install frontend dependencies
- does not modify project repositories

Replacement behavior:

- `--replace` moves existing skill folders into a timestamped backup folder before copying replacements
- review the dry run before replacing anything

Recommended first command:

```bash
python3 scripts/install_skills.py --dry-run
```

## Reporting Issues

For a potential vulnerability, use this repository's private vulnerability reporting flow. Do not include secrets, exploit steps, or sensitive paths in a public issue.

Open a public GitHub issue for:

- non-sensitive installer behavior
- documentation errors
- skill-quality or usability issues

## Maintainer Safety Standard

Any code-changing skill should prefer:

- inspecting repo state before edits
- creating a branch or checkpoint before risky work
- listing planned edits
- keeping destructive operations explicit
- running available verification commands
- explaining restore or revert options

These principles are also encoded in the `code-change-safety-checkpoint` and `code-change-undo-revert` skills.
