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

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.
