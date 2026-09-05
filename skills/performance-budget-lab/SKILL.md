---
name: performance-budget-lab
description: "Set performance budgets before implementation."
---

# Performance Budget Lab

Use this skill to keep visually rich sites fast.

Own the budget and acceptance policy. Route measured runtime diagnosis, implementation fixes, and React/Next performance work to `$performance-audit-websites`.

## Budget Areas

- JavaScript bundle size
- route-level code splitting
- image dimensions, formats, and lazy loading
- video poster, preload, autoplay, and reduced-data behavior
- font loading and fallback metrics
- animation cost and scroll handlers
- layout shift sources
- server rendering/static rendering choices
- caching and CDN behavior

## Workflow

1. Identify stack and deployment target.
2. Inspect package dependencies and route structure.
3. Define route, hardware/device, network/cache state and measurement method.
4. Run Lighthouse or browser performance checks when feasible.
5. Check Core Web Vitals risks: LCP, CLS, INP, TTFB.
6. Set media/JavaScript/font budgets from the intended experience and baseline evidence.
7. Prefer CSS and Motion for small interactions; reserve GSAP/R3F/video for clear value.
8. Report tradeoffs honestly when visual richness costs performance.

Use Lighthouse or browser checks here to validate a budget decision, not to take ownership of deep runtime diagnosis. When the work shifts from setting thresholds to locating and repairing the bottleneck, hand off to `$performance-audit-websites`.

## Output

Give:

- current risks
- recommended budgets
- measurement conditions and reconsideration rules
- commands run
- remaining uncertainty

## Scope and evidence

Output a budget contract: route/device class, hardware, network/cache state, metric, threshold, test method and reconsideration condition. Route measured diagnosis/optimization to `$performance-audit-websites`; a budget-only request does not implement repairs.
