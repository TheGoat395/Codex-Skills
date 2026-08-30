# Cursor Adapter

Cursor uses project rules rather than loading this repo's full `skills/` tree. The adapter in this folder gives Cursor a compact project-rule version of the public core's frontend and agent-quality standards.

## Install

From a target project:

```bash
mkdir -p .cursor/rules
cp path/to/Codex-Skills/adapters/cursor/codex-premium-website-skills.mdc .cursor/rules/
```

Then open the project in Cursor and use the rule while working on frontend, website, motion, QA, agent reasoning, or handoff tasks.

## Best Use

Use this adapter when you want Cursor to apply the repo's standards without installing all 80 skills:

- infer the brief before building
- avoid generic AI website patterns
- use stronger typography, layout, and visual assets
- inspect responsive behavior
- respect accessibility and reduced motion
- distinguish evidence, inference, assumptions, and unknowns
- verify failures and completion claims with fresh checks
- summarize verification before handoff

## What This Adapter Is

- A compact rules file for Cursor.
- A practical summary of the public core.
- A good starting point for website, frontend, and agent-workflow projects.

## What This Adapter Is Not

- Not a full replacement for every `SKILL.md`.
- Not a tested one-to-one install of all 80 skills into Cursor.
- Not an endorsement by Cursor.

For the full source instructions, inspect the `skills/` directory.
