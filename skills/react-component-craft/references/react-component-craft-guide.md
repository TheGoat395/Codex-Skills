# React Component Craft Guide

## Lens

Good components express local design patterns and keep the page easy to revise.

## Rules

- Extract components when it improves clarity or reuse.
- Keep content close unless a content model helps editing.
- Use semantic HTML first, ARIA only when needed.
- Expose useful props, not every possible style option.
- Make fixed-format UI dimensions stable.

## Useful Patterns

- Section component with heading, copy, media, and layout concerns.
- Primitive button/link with variants and icon support.
- Reusable reveal wrapper with reduced-motion support.
- Data-driven repeated items where the content is truly repeated.

## Avoid

- Card components nested inside card components.
- Over-abstracted layout wrappers that hide the design.
- Prop soup for one-off sections.

## Acceptance Criteria

- Components are readable and fit the local design system.
- Interaction and responsive states are handled.

## Shared Requirements

- Inspect before coding: structure, framework, homepage or main entry file, styling system, JavaScript or interaction system, assets, and build commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, or fix.
- Use existing project conventions first. Explain major new dependencies before adding them.
- Never ship generic visual work: no default card grids, placeholder copy, weak type, random gradients, stock-like media, or template heroes.
- Build version 1, inspect the rendered result, improve spacing, type, hierarchy, motion, media, hover states, and responsiveness, then run checks again.
- Run available lint, build, and test commands when possible. Report commands, changed files, and any untested areas honestly.
- Check desktop and mobile. Respect accessibility, semantic markup, focus states, and reduced-motion preferences.
