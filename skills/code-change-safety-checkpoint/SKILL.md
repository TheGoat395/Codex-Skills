---
name: code-change-safety-checkpoint
description: "Preserve rollback before materially risky edits."
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
   - Follow the current repository/worktree branch policy. Record a recoverable base commit for tracked data; a branch label alone does not preserve uncommitted or untracked files.
   - If the repo has user changes, preserve the affected hunks and untracked targets with an appropriate patch, snapshot or scoped backup when the edit could destroy them. Avoid redundant copies of already protected targets.
   - If there is no git repo or the work involves generated assets, make a timestamped local backup of the files or folders you will touch.

3. Explain planned edits before changing files.
   - List the main files or directories you expect to edit.
   - Call out any deletion, move, or overwrite.
   - A clear task instruction authorizes routine in-scope edits regardless of its verbs. Ask only for a materially ambiguous destructive target or another genuinely missing authorization.

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
