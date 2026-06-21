# React Accessible Components Guide

## Purpose

Make polished UI actually usable by keyboard, screen reader, and reduced-motion users.

## Use When

- A visible React component is interactive.
- The UI includes menus, modals, accordions, tabs, forms, icon buttons, carousels, cards, or navigation.
- A premium site needs accessible focus, hover, active, disabled, loading, and error states.

## Do Not Use When

- The task is pure content editing with no UI behavior.
- A proven accessible primitive library is already used correctly and no new component is added.
- The project is non-React and another accessibility skill applies better.

## Discovery Questions

- Is the element a button, link, input, heading, list, landmark, or disclosure semantically?
- How does the component work with keyboard only?
- What is the accessible name and state?
- Where should focus move when opening, closing, submitting, or navigating?

## Decision Tree

- Start with semantic HTML before ARIA.
- If a component is complex, prefer Radix/shadcn-style primitives where already available.
- If building custom behavior, define keyboard support before animation polish.
- If using icons only, add accessible labels and tooltips where helpful.
- If motion changes focus or visibility, respect reduced-motion preferences.

## Implementation Rules

- Use `<button>` for actions and `<a>`/`Link` for navigation.
- Never remove visible focus without replacing it with a clear custom focus style.
- Make disabled/loading states programmatically and visually clear.
- Labels, errors, descriptions, and required state must connect to fields.
- Do not use ARIA to disguise non-semantic div soup.

## Useful Patterns

- Icon button: visible icon, `aria-label`, stable square size, focus ring, disabled state.
- Dialog: focus trap, escape/overlay close, labelled title, restore focus, scroll lock.
- Tabs: roving focus or library primitive, selected state, panel association.

## Anti-Patterns

- Clickable divs.
- Hover-only content needed for comprehension.
- Focus rings hidden because they look less sleek.
- Menus that animate beautifully but cannot be operated with keyboard.

## QA Checklist

- Tab through the changed UI.
- Test Enter/Escape/Space/Arrow behavior where relevant.
- Check accessible names for icon buttons and fields.
- Run available accessibility lint/audit tools when present.

## Acceptance Criteria

- The component works without a mouse.
- Semantics match behavior.
- Accessibility states look designed, not bolted on.

## Shared Website Requirements

- Inspect before coding: project structure, framework, router, homepage or main entry, styling system, JavaScript or motion system, assets, and available commands.
- Prefer the existing project stack and conventions before adding dependencies or moving architecture.
- For Next.js App Router projects, keep Server Components as the default and introduce Client Components only for interactivity, browser APIs, effects, or client-only libraries.
- For React work, keep components pure, derive render data during render, and use Effects only to synchronize with external systems.
- Default website output must still follow the premium visual baseline: strong type, real content, designed states, responsive polish, and no generic card-grid filler.
- Run available lint, build, test, and local browser checks when possible; report exactly what ran and what was not tested.
- Check desktop and mobile behavior when changing visible UI, especially overflow, focus, loading, empty, error, and reduced-motion states.

## Official Source Anchors

- React Learn: https://react.dev/learn
- React reference: https://react.dev/reference/react
- Next.js docs overview: https://nextjs.org/docs
