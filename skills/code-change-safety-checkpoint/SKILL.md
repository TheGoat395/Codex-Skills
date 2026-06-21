---
name: code-change-safety-checkpoint
description: Preserve a rollback path before risky code or website edits. Use when changes may touch many files, delete files, overwrite generated output, alter user work, refactor shared behavior, modify deployment config, or otherwise risk losing working code.
---

# Code Change Safety Checkpoint

Use this skill before risky edits. The goal is simple: make sure there is a credible way back before changing files.

## Trigger

Use when:

- the user asks for website, app, repo, or code changes with nontrivial blast radius
- files may be deleted, moved, regenerated, overwritten, or mass-edited
- the repo has uncommitted changes
- the work touches shared behavior, routing, deployment config, generated assets, or build tooling
- the user specifically asks for backup, checkpoint, rollback protection, or protection from accidental destructive changes

Do not run heavy backup steps for tiny read-only analysis or single-line edits unless the user asks.

## Workflow

1. Inspect state before editing.
   - Run `git status --short --branch` when inside a git repo.
   - Identify changed files that already exist before your work.
   - Treat uncommitted user changes as protected.

2. Choose the rollback path.
   - If the repo is clean, create a new branch for substantial work.
   - If the repo has user changes, avoid overwriting them and describe the risk.
   - If there is no git repo or the work involves generated assets, make a timestamped local backup of the files or folders you will touch.

3. Explain planned edits before changing files.
   - List the main files or directories you expect to edit.
   - Call out any deletion, move, or overwrite.
   - Ask for confirmation unless the user clearly said proceed, build, create, implement, fix, or continue.

4. Edit narrowly.
   - Avoid unrelated refactors.
   - Do not revert user changes unless explicitly requested.
   - Prefer additive changes when the risk is unclear.

5. Report the restore path.
   - Branch name, backup path, or commit/checkpoint strategy.
   - Commands or steps needed to undo your work.

## Restore Guidance

For git-backed work, useful restore options include:

```bash
git status --short
git diff
git restore path/to/file
git switch main
```

Use destructive restore commands only when explicitly requested. Never run `git reset --hard` as a casual cleanup step.

For local backups, explain the backup folder and which files can be copied back.
