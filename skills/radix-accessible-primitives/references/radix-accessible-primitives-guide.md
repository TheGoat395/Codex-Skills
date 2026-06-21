# Radix Accessible Primitives Guide

## Purpose

Get robust interaction semantics while keeping full control over visual design.

## Use When

- A custom interactive component would otherwise require complex keyboard and focus behavior.
- The project already uses Radix directly or through shadcn/ui.
- Dialogs, menus, popovers, tabs, tooltips, accordions, switches, or selects need to be accessible and custom-styled.

## Do Not Use When

- A native HTML element fully solves the interaction.
- The project uses a different accessible component library consistently.
- The task is visual-only and no interactive primitive is needed.

## Discovery Questions

- Which user interaction pattern is needed and does Radix provide it?
- What semantics, keyboard behavior, and focus management are required?
- How should data-state and data-disabled attributes map to styling?
- Does the primitive need controlled or uncontrolled state?

## Decision Tree

- Choose native HTML first when it is enough.
- Use Radix for complex composite widgets that need proven accessibility behavior.
- Style parts with project tokens and data attributes.
- Keep focus management, portals, refs, and aria attributes intact.
- Test keyboard and screen-reader-relevant behavior after styling.

## Implementation Rules

- Do not remove Radix props, refs, or data attributes without understanding the behavior.
- Style every state: open, closed, highlighted, selected, disabled, checked, unchecked.
- Keep overlay, portal, and z-index behavior coordinated with the design system.
- Use tooltips for supplementary hints, not required information.
- Prefer predictable interaction patterns over novelty for controls.

## Useful Patterns

- Dropdown menu: trigger, content, item, separator, shortcut, disabled, focus/highlight.
- Dialog: title, description, close, overlay, content, focus restore, mobile sizing.
- Tabs: list, trigger, selected state, panel, keyboard navigation.
- Switch/radio/checkbox: visible state, label, focus ring, disabled behavior.

## Anti-Patterns

- Rebuilding a complex menu from divs and click handlers.
- Animating Radix content while ignoring focus and escape behavior.
- Hiding labels because the primitive seems to work visually.
- Using Radix for simple static layout.

## QA Checklist

- Test keyboard behavior: Tab, Shift+Tab, Enter, Space, Escape, Arrow keys where relevant.
- Check focus trap and restore for dialogs/popovers.
- Inspect open/closed/selected/disabled styles.
- Run available accessibility checks.

## Acceptance Criteria

- The component behaves like the expected accessible pattern.
- Styling is custom and premium, not default or generic.
- Accessibility remains intact after visual customization.

## Shared Website Requirements

- Inspect before coding: project structure, framework, styling system, token files, component primitives, entry CSS, build commands, and existing visual conventions.
- Prefer the existing styling approach before introducing Tailwind, shadcn/ui, Radix, class-variance tools, or custom CSS architecture.
- Use design tokens to make choices repeatable, but keep the site-specific art direction alive. Tokens should support taste, not flatten it.
- Avoid generic AI website tells: default card grids, template spacing, random gradients, one-note palettes, weak buttons, unstyled forms, and placeholder copy.
- Check desktop and mobile. Prevent overflow, text collisions, unstable control sizes, inaccessible focus, and broken media crops.
- Respect accessibility, color contrast, keyboard navigation, focus-visible states, and reduced-motion preferences.
- Run available lint, build, test, and local browser checks when possible; report exact commands and untested areas.

## Official Source Anchors

- Radix Primitives introduction: https://www.radix-ui.com/primitives/docs/overview/introduction
- shadcn/ui docs: https://ui.shadcn.com/docs
- MDN focus-visible: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible
