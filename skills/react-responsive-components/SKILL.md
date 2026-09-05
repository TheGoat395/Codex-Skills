---
name: react-responsive-components
description: "Implement size-dependent behavior/geometry."
---

# React Responsive Components

For substantial web work, reuse the [scoped web contract](../website-operating-rules/references/scoped-web-contract.md) when available; it replaces duplicated policy here. Match the requested scope and existing decisions; a missing optional sibling does not block this local procedure.

## Use This Skill

Use this skill to build responsive react components that do not collapse on mobile.

## Required Reference

Read [references/react-responsive-components-guide.md](references/react-responsive-components-guide.md) before making architectural or visible UI changes with this skill.

## Ownership

Own responsive interaction/state or measured geometry when React is needed. Solve layout with CSS first; use `tailwind-responsive-layouts` for Tailwind layout implementation. Do not add measurement state or duplicate DOM trees for a CSS-only problem.
