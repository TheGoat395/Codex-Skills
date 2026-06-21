---
name: code-change-undo-revert
description: Undo or revert code changes safely. Use when the user asks to undo, revert, roll back, restore, recover, go back, remove recent changes, or compare current work against a previous checkpoint.
---

# Code Change Undo And Revert

Use this skill when the user wants to go back safely. The job is to identify what changed, preserve user work, and choose the least destructive undo path.

## Trigger

Use when the user says:

- undo
- revert
- roll back
- restore
- recover
- go back to before
- remove your changes
- bring back deleted code
- compare against the checkpoint

## Workflow

1. Inspect the current state.
   - Run `git status --short --branch` when in a git repo.
   - Review changed files before reverting anything.
   - Identify whether changes are yours, the user's, generated output, or mixed.

2. Choose the safest target.
   - If the user wants only your latest edits undone, revert only those files or hunks.
   - If the user wants a branch or commit reverted, inspect the commit range first.
   - If a local backup exists, compare backup files before copying anything back.

3. Avoid broad destructive commands.
   - Do not run `git reset --hard`, `git clean -fd`, or branch deletion unless explicitly requested and confirmed.
   - Do not remove untracked files until you know they are safe to delete.
   - Do not overwrite user edits mixed into a file unless the user approves.

4. Apply the revert.
   - Prefer `git restore path/to/file` for clearly scoped tracked files.
   - Prefer patch-level edits when user and assistant changes are mixed.
   - Prefer copying from a timestamped backup only for files known to belong to the requested rollback.

5. Verify and report.
   - Run relevant tests, builds, or diff checks when possible.
   - Summarize what was restored, what remains changed, and any files intentionally left alone.

## User Communication

Be explicit:

- what checkpoint or commit you are reverting to
- which files will change
- which files contain user changes and are being preserved
- which commands were run
- how to inspect the result
