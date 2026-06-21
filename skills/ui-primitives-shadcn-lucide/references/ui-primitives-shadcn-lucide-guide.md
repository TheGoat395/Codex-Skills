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

## Shared Requirements

- Inspect before coding: structure, framework, homepage or main entry file, styling system, JavaScript or interaction system, assets, and build commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, or fix.
- Use existing project conventions first. Explain major new dependencies before adding them.
- Never ship generic visual work: no default card grids, placeholder copy, weak type, random gradients, stock-like media, or template heroes.
- Build version 1, inspect the rendered result, improve spacing, type, hierarchy, motion, media, hover states, and responsiveness, then run checks again.
- Run available lint, build, and test commands when possible. Report commands, changed files, and any untested areas honestly.
- Check desktop and mobile. Respect accessibility, semantic markup, focus states, and reduced-motion preferences.
