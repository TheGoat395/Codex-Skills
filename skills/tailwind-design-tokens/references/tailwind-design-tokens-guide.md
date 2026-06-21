# Tailwind Design Tokens Guide

## Lens

Tailwind is fast, but the taste comes from tokens, constraints, and repeated decisions.

## Rules

- Define CSS variables for role-based colors and surfaces.
- Use repeatable spacing rhythm with deliberate exceptions.
- Centralize button, link, focus, and container patterns.
- Use clamp, minmax, aspect-ratio, and max-width to stabilize layouts.

## Useful Patterns

- globals.css: tokens, base typography, selection, focus, reduced motion.
- cn helper for class composition.
- Component variants for buttons, tags, nav links, and surface panels.
- Container utilities with named widths.

## Avoid

- One-off hex colors everywhere.
- Random spacing values with no rhythm.
- Default Tailwind gray/purple look when the brand needs distinction.

## Acceptance Criteria

- The visual system can be adjusted from tokens.
- Utilities express design decisions consistently.

## Shared Requirements

- Inspect before coding: structure, framework, homepage or main entry file, styling system, JavaScript or interaction system, assets, and build commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, or fix.
- Use existing project conventions first. Explain major new dependencies before adding them.
- Never ship generic visual work: no default card grids, placeholder copy, weak type, random gradients, stock-like media, or template heroes.
- Build version 1, inspect the rendered result, improve spacing, type, hierarchy, motion, media, hover states, and responsiveness, then run checks again.
- Run available lint, build, and test commands when possible. Report commands, changed files, and any untested areas honestly.
- Check desktop and mobile. Respect accessibility, semantic markup, focus states, and reduced-motion preferences.
