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

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.

## Version-aware token consumption

Inspect the installed Tailwind version and existing CSS/configuration entry before changing token mappings. In Tailwind v4, `@theme` namespace variables define utility-facing tokens; ordinary `:root` custom properties do not automatically create matching utilities. Use `@theme inline` when an alias should reference another variable at the utility usage site, and test generated CSS and theme switching. Keep existing version-specific configuration in older projects; this skill does not authorize a Tailwind migration. [Theme variables](https://tailwindcss.com/docs/theme).
