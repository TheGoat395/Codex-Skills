---
name: code-change-undo-revert
description: "Restore requested code changes or checkpoints."
---

# Code Change Undo And Revert

Use this skill when the user wants to go back safely. The job is to identify what changed, preserve user work, and choose the least destructive undo path.

## Trigger

Use these phrases only when the surrounding request establishes code/repository rollback intent:

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
   - Do not run `git reset --hard`, `git clean -fd`, or branch deletion unless explicitly authorized for the resolved scope. Do not seek a second confirmation for an already precise authorization.
   - Do not remove untracked files until you know they are safe to delete.
   - Do not overwrite user edits mixed into a file unless the user approves.

4. Apply the revert.
   - Use `git restore` for the explicitly selected working-tree/index state; inspect its source first. Use `git revert <commit>` to reverse a committed change while preserving history when that is the requested operation.
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
