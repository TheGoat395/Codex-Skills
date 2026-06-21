# CSS Grid Editorial Systems Guide

## Purpose

Use grid to create hierarchy, rhythm, and editorial taste instead of default equal cards.

## Use When

- A page needs a premium layout with varied scale, media, and content hierarchy.
- A generic card grid should become an editorial or product-proof composition.
- Galleries, portfolios, case studies, homepage sections, or feature narratives need stronger structure.

## Do Not Use When

- A simple one-dimensional alignment problem is better solved with flexbox.
- The content is tabular and should use a table or data grid.
- The existing design system already prescribes grid behavior.

## Discovery Questions

- What is the visual hierarchy: lead item, secondary items, supporting proof, or archive?
- What grid constraints exist: columns, gutters, max width, baseline rhythm, media aspect ratios?
- Should the layout be symmetric, asymmetric, dense, spacious, editorial, or operational?
- How should the grid collapse on mobile without becoming a bland stack?

## Decision Tree

- Define content roles before grid tracks.
- Use explicit grid tracks for major composition and auto-placement for repeated minor items.
- Use aspect-ratio and object-fit for stable media plates.
- Vary scale intentionally: one lead moment, a few supporting pieces, and calm spacing.
- Create a mobile order that preserves narrative priority.

## Implementation Rules

- Do not use equal cards when the content has unequal importance.
- Keep gutters and alignment consistent even in asymmetry.
- Avoid layout tricks that break reading order or keyboard order.
- Use grid areas or named classes when the composition is complex enough.
- Make image crops and captions part of the grid system.

## Useful Patterns

- Portfolio: one oversized feature, two medium works, compact archive strip.
- Luxury editorial: full-bleed media band, offset text column, restrained supporting grid.
- Product proof: large UI screenshot, adjacent metric/code/details, integration row.
- Case study: artifact plates with alternating span and caption behavior.

## Anti-Patterns

- Three identical cards under every heading.
- Masonry-like layouts that create chaotic reading order.
- Grid spans chosen randomly for visual noise.
- Desktop-only editorial grid with broken mobile order.

## QA Checklist

- Inspect reading order, tab order, and mobile order.
- Check all media aspect ratios and crops.
- Verify grid does not overflow at mid-widths.
- Compare the result against the section's hierarchy goals.

## Acceptance Criteria

- The grid communicates content priority clearly.
- The layout feels authored and site-specific.
- Mobile keeps the editorial rhythm instead of collapsing into generic cards.

## Shared Website Requirements

- Inspect before coding: project structure, framework, styling system, token files, component primitives, entry CSS, build commands, and existing visual conventions.
- Prefer the existing styling approach before introducing Tailwind, shadcn/ui, Radix, class-variance tools, or custom CSS architecture.
- Use design tokens to make choices repeatable, but keep the site-specific art direction alive. Tokens should support taste, not flatten it.
- Avoid generic AI website tells: default card grids, template spacing, random gradients, one-note palettes, weak buttons, unstyled forms, and placeholder copy.
- Check desktop and mobile. Prevent overflow, text collisions, unstable control sizes, inaccessible focus, and broken media crops.
- Respect accessibility, color contrast, keyboard navigation, focus-visible states, and reduced-motion preferences.
- Run available lint, build, test, and local browser checks when possible; report exact commands and untested areas.

## Official Source Anchors

- MDN CSS grid layout: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout
- Tailwind utility classes: https://tailwindcss.com/docs/styling-with-utility-classes
- Tailwind responsive design: https://tailwindcss.com/docs/responsive-design
