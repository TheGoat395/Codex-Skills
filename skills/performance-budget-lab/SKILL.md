---
name: performance-budget-lab
description: "Define website performance budgets and pre-build acceptance constraints. Use for numeric bundle/media/font/route budgets, Core Web Vitals targets, visual-richness tradeoffs, CI budget policy, and deciding what a premium site may spend before implementation; not for diagnosing or fixing a measured React/Next/runtime regression."
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
3. Run available build/lint/test commands.
4. Run Lighthouse or browser performance checks when feasible.
5. Check Core Web Vitals risks: LCP, CLS, INP, TTFB.
6. Optimize media before adding more JS.
7. Prefer CSS and Motion for small interactions; reserve GSAP/R3F/video for clear value.
8. Report tradeoffs honestly when visual richness costs performance.

Use Lighthouse or browser checks here to validate a budget decision, not to take ownership of deep runtime diagnosis. When the work shifts from setting thresholds to locating and repairing the bottleneck, hand off to `$performance-audit-websites`.

## Output

Give:

- current risks
- recommended budgets
- concrete fixes
- commands run
- remaining uncertainty
