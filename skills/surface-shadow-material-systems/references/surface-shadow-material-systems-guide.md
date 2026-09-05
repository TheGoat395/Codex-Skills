# Surface Shadow Material Systems Guide

## Purpose

Make depth and surfaces support hierarchy instead of decorating everything.

## Use When

- A UI uses cards, panels, modals, popovers, sticky nav, product mockups, or dashboard surfaces.
- The page looks flat, muddy, over-shadowed, or default-library-like.
- Luxury/editorial/product polish depends on material nuance.

## Do Not Use When

- A strict flat design system forbids shadows/material treatment.
- The task is unrelated to visible surfaces.
- A small copy fix should not alter visual hierarchy.

## Discovery Questions

- What levels of surface are needed: page, section, panel, raised, overlay, selected, disabled?
- Should depth come from border, shadow, color, blur, texture, or spacing?
- What radius scale fits the brand and platform?
- Are cards actually needed, or would bands, grids, tables, or media sections be better?

## Decision Tree

- Define surface levels before styling components.
- Use borders and subtle color shifts before large shadows where possible.
- Reserve heavy elevation for overlays, active panels, or true hierarchy.
- Keep radius consistent and usually modest for professional sites.
- Avoid cards inside cards and decorative glass without concept.

## Implementation Rules

- Do not use glassmorphism, blur, blobs, or glow as default premium styling.
- Treat 8px or less as one restrained starting point; use optically tested radii that fit the approved brand, material and component scale.
- Surfaces must clarify grouping, state, or hierarchy.
- Use shadows that match light direction and background.
- Make dark-mode elevation rely more on borders/tints than opaque shadows.

## Useful Patterns

- Product UI: page background, panel surface, raised active state, popover overlay.
- Luxury editorial: minimal panels, fine dividers, material image plates, soft section contrast.
- Dashboard: dense panels with low-radius edges, clear dividers, restrained elevation.

## Anti-Patterns

- Every section as a floating card.
- Nested cards to solve spacing.
- Large blurry shadows on every object.
- Random glass panels over unrelated gradients.

## QA Checklist

- Scan for nested cards and excessive shadows.
- Check surface hierarchy in light and dark contexts.
- Inspect modals/popovers/sticky nav over page content.
- Verify borders and shadows remain visible on mobile screens.

## Acceptance Criteria

- Surfaces create readable hierarchy.
- Depth feels restrained and project-specific.
- The UI avoids generic card/glass visual tropes.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- Tailwind utility classes: https://tailwindcss.com/docs/styling-with-utility-classes
- Tailwind theme variables: https://tailwindcss.com/docs/theme
- MDN CSS custom properties: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*
