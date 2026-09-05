# UI Primitives Shadcn Lucide Guide

## Lens

Accessible primitives save time, but default styling is not design direction.

## Rules

- Use shadcn/ui for behavior and accessibility when the project already uses it or the component complexity warrants it.
- Customize tokens, radii, borders, focus, hover, spacing, and icons to match the site.
- Use lucide icons for familiar tool or command buttons.
- Use labels/tooltips for unfamiliar icons.

## Useful Patterns

- Dialog: strong focus handling, restrained surface, clear action row.
- Tabs: visible active state and keyboard support.
- Forms: labels, helper text, errors, disabled/loading states.
- Icon buttons: stable square dimensions and tooltip.

## Avoid

- Dropping default shadcn components into a luxury/editorial page unchanged.
- Text buttons where a familiar icon control is clearer.
- Icon-only controls with no accessible label.

## Acceptance Criteria

- Primitives feel native to the site design.
- Accessibility basics remain intact.

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.
