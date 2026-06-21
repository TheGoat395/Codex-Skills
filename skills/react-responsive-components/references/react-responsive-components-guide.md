# React Responsive Components Guide

## Purpose

Make mobile layouts intentionally composed rather than merely stacked.

## Use When

- A React component or page must work across mobile, tablet, and desktop.
- A premium site has text overflow, cramped buttons, broken media crops, card stacking, or horizontal scroll.
- The component has fixed-format UI such as boards, toolbars, grids, galleries, counters, or tiles.

## Do Not Use When

- The change is not visible or has no layout impact.
- A one-off desktop-only internal tool is explicitly requested.
- The project is not React and a CSS-specific skill applies better.

## Discovery Questions

- Which breakpoints or container widths does the existing system use?
- What must remain visible or actionable on mobile?
- Which elements need stable dimensions to prevent layout shift?
- Can CSS solve this without JavaScript measurement?

## Decision Tree

- Start CSS-first with grid, flex, clamp limits, aspect ratio, min/max, and container-aware patterns.
- Use JavaScript measurement only when layout depends on real runtime geometry.
- Design mobile composition separately; do not rely on automatic stacking for premium pages.
- Lock stable dimensions for controls, boards, tiles, and media frames.
- After editing, inspect at least one mobile and one desktop viewport.

## Implementation Rules

- Do not scale font size directly with viewport width.
- Prevent horizontal overflow and long-word breakage.
- Use aspect-ratio and object-fit for media crops.
- Keep tap targets comfortable and icons/text from colliding.
- Avoid nested cards and cramped card stacks on mobile.

## Useful Patterns

- Editorial section: desktop asymmetric grid, mobile reordered media and copy with designed rhythm.
- Product UI: desktop dense mockup, mobile cropped/stacked views with zoomed details.
- Dashboard: responsive table strategy, filters collapse, core metric remains visible.

## Anti-Patterns

- Desktop layout with `scale(.7)` on mobile.
- Hero text that overlaps media at mid-widths.
- Icon buttons that resize because labels or hover states change.
- Cards nested in cards to solve spacing.

## QA Checklist

- Check common widths around 390, 768, 1024, and 1440 when possible.
- Inspect horizontal scroll and text overflow.
- Test hover-only affordances on touch.
- Verify media crops show the actual subject.

## Acceptance Criteria

- The component feels designed at mobile and desktop sizes.
- No visible overlap, overflow, or accidental resizing occurs.
- Responsive behavior supports the site's visual direction.

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
- Image optimization: https://nextjs.org/docs/app/getting-started/images
