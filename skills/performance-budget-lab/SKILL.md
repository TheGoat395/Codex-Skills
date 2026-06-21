---
name: performance-budget-lab
description: "Use for website performance planning, Lighthouse/web-vitals checks, bundle/media/font budgets, Core Web Vitals triage, image/video optimization, animation performance, deployment readiness, and premium-site speed audits."
---

# Performance Budget Lab

Use this skill to keep visually rich sites fast.

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

## Output

Give:

- current risks
- recommended budgets
- concrete fixes
- commands run
- remaining uncertainty
