# Tailwind Responsive Layouts Guide

## Purpose

Make Tailwind responsive behavior feel composed rather than mechanically stacked.

## Use When

- A Tailwind page or component must work across mobile, tablet, desktop, and wide screens.
- The design has text overflow, cramped controls, broken image crops, awkward stacked sections, or horizontal scroll.
- A homepage, portfolio, product page, commerce layout, or dashboard needs responsive layout decisions.

## Do Not Use When

- The project does not use Tailwind.
- The component has no visible layout or breakpoint behavior.
- The existing design system already prescribes exact responsive rules.

## Discovery Questions

- What are the existing breakpoints and container conventions?
- Which content must stay visible on small screens?
- Which elements need stable aspect ratio, fixed control size, or alternate ordering?
- Should responsiveness depend on viewport breakpoints or component container size?

## Decision Tree

- Start mobile-first and add breakpoint variants only where layout actually changes.
- Use container width, max-width, grid tracks, flex behavior, gap, and aspect-ratio as the primary tools.
- Use container queries or CSS when component context matters more than viewport width.
- Create separate mobile composition for hero/media-heavy sections rather than only stacking desktop blocks.
- Inspect at narrow, tablet, desktop, and wide widths after implementation.

## Implementation Rules

- Do not scale font size directly with viewport width.
- Use stable dimensions for buttons, icon controls, galleries, cards, tiles, and mockups.
- Make media crops reveal the subject at every breakpoint.
- Limit breakpoint soup. Each responsive class should have a visible reason.
- Keep text readable with sensible line length, wrapping, and spacing.

## Useful Patterns

- Hero: mobile media below or behind text with safe contrast; desktop composed with asymmetry or full bleed.
- Editorial grid: one-column mobile rhythm, tablet paired media/text, desktop asymmetric grid.
- Product UI mockup: mobile crop/detail view, desktop full workflow view.
- Dashboard: mobile summary and filters, desktop dense table/chart layout.

## Anti-Patterns

- Adding `sm:`, `md:`, `lg:`, and `xl:` variants to every utility by reflex.
- Using `scale-*` to shrink desktop layouts on mobile.
- Mobile views that are just a stack of identical cards.
- Long words, button labels, or code blocks causing horizontal overflow.

## QA Checklist

- Check at least one mobile and one desktop viewport, plus mid-width if possible.
- Inspect horizontal scroll, text wrapping, tap targets, and image crops.
- Test nav, forms, galleries, and sticky elements on mobile.
- Run build/lint to catch invalid classes.

## Acceptance Criteria

- Responsive Tailwind classes are purposeful and sparse.
- Mobile layout feels intentionally composed.
- No visible overflow, overlap, or accidental resizing remains.

## Shared Website Requirements

- Inspect before coding: project structure, framework, styling system, token files, component primitives, entry CSS, build commands, and existing visual conventions.
- Prefer the existing styling approach before introducing Tailwind, shadcn/ui, Radix, class-variance tools, or custom CSS architecture.
- Use design tokens to make choices repeatable, but keep the site-specific art direction alive. Tokens should support taste, not flatten it.
- Avoid generic AI website tells: default card grids, template spacing, random gradients, one-note palettes, weak buttons, unstyled forms, and placeholder copy.
- Check desktop and mobile. Prevent overflow, text collisions, unstable control sizes, inaccessible focus, and broken media crops.
- Respect accessibility, color contrast, keyboard navigation, focus-visible states, and reduced-motion preferences.
- Run available lint, build, test, and local browser checks when possible; report exact commands and untested areas.

## Official Source Anchors

- Tailwind utility classes: https://tailwindcss.com/docs/styling-with-utility-classes
- Tailwind responsive design: https://tailwindcss.com/docs/responsive-design
- MDN CSS container queries: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries
