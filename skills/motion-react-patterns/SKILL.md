---
name: motion-react-patterns
description: "Implement Motion APIs, presence and lifecycle."
---

# Motion React Patterns

For substantial web work, reuse the [scoped web contract](../website-operating-rules/references/scoped-web-contract.md) when available; it replaces duplicated policy here. Match the requested scope and existing decisions; a missing optional sibling does not block this local procedure.

## Use This Skill

Use this skill to use motion for react microinteractions and component animation.

## Required Reference

Read [references/motion-react-patterns-guide.md](references/motion-react-patterns-guide.md) before making architectural or visible UI changes with this skill.

## Ownership

Own Motion APIs, animation state and lifecycle. Route shared layout to `motion-react-layout-transitions`, navigation to `motion-react-page-transitions`, and new feedback/timing direction to `motion-react-microinteractions` only when those decisions are needed.
