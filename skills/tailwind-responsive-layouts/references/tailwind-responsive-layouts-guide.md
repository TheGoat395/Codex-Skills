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
- Existing responsive behavior is already correct and the request neither changes nor reviews it. When implementation or repair is requested, follow the exact existing design-system rules rather than inventing new breakpoints.

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

- Avoid unbounded `vw`-only typography. Bounded fluid type such as `clamp()` with readable minimum/maximum and font-relative sizing is valid; test zoom, reflow and long content.
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

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.

## Official Source Anchors

- Tailwind utility classes: https://tailwindcss.com/docs/styling-with-utility-classes
- Tailwind responsive design: https://tailwindcss.com/docs/responsive-design
- MDN CSS container queries: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries

Preserve semantic DOM reading and keyboard order across responsive arrangements; visual reordering must not create a conflicting interaction sequence. Test the supported viewport scope rather than imposing a mobile rebuild on an explicitly desktop-only brief.
