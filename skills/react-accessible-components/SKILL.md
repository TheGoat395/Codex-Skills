---
name: react-accessible-components
description: "Implement semantic names, keyboard and focus."
---

# React Accessible Components

For substantial web work, reuse the [scoped web contract](../website-operating-rules/references/scoped-web-contract.md) when available; it replaces duplicated policy here. Match the requested scope and existing decisions; a missing optional sibling does not block this local procedure.

## Use This Skill

Use this skill to build accessible react controls, navigation, and interactive ui.

## Required Reference

Read [references/react-accessible-components-guide.md](references/react-accessible-components-guide.md) before making architectural or visible UI changes with this skill.

## Ownership

Own semantic HTML, accessible names, keyboard/focus and programmatic state. Use the current primitive implementation; detailed Radix APIs belong to `radix-accessible-primitives` only when Radix is actually used. An accessibility repair does not require a styling redesign.
