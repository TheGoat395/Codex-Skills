---
name: performance-audit-websites
description: "Measure, diagnose, or improve website runtime performance. Use for Core Web Vitals, LCP, INP, CLS, Lighthouse/browser diagnosis, React or Next.js waterfalls and rendering, bundle and hydration cost, media/fonts, third parties, animation cost, and evidence-backed implementation fixes; not for defining the project's initial performance-budget policy."
---

# Performance Audit Websites

Use this skill to keep premium sites fast enough that visual ambition does not punish users. Measure first and optimize the dominant constraint; do not apply framework folklore as proof.

Own measured diagnosis and implementation. Route pre-build numeric budgets, acceptance thresholds, and visual-richness policy to `$performance-budget-lab`.

## Workflow

1. Inspect the project, scripts, routes, local/deployed URL, production surfaces, and available QA/deployment tooling.
2. Read [Performance Audit Websites Guide](references/performance-audit-websites-guide.md) before claiming the site is ready. For React or Next.js implementation work, also read [React and Next.js performance](references/react-next-performance.md).
3. Run the narrowest meaningful checks for the risk: visual, mobile, accessibility, performance, forms, media, SEO, analytics, deployment, or handoff.
4. Fix issues when they are in scope; otherwise record exact evidence and remaining risk.
5. Summarize commands, URLs, screenshots/checks, changed files, and what was not tested.

Separate field data, controlled lab data, source inspection, and inference. A Lighthouse score from one machine is not a field-performance guarantee; an optimized source pattern is not a measured user improvement.

## Always Protect

- Inspect before changing or shipping: framework, package scripts, build output, routes, forms, media, animation stack, deployment target, environment variables, analytics, SEO metadata, accessibility risks, and available browser QA tooling.
- Do not claim something was tested unless it was actually tested; report exact commands, URLs, screenshots, viewports, failures, skipped checks, and remaining risk.
- Verify desktop and mobile rendered output, not only source code. For visual or motion work, inspect screenshots, browser behavior, console errors, network failures, and responsive layout.
- Treat forms, checkout, booking, CMS content, analytics, environment variables, and deployments as production surfaces with error, loading, empty, success, and rollback states.
- Respect accessibility, performance, reduced-motion, and no-JavaScript/no-WebGL/no-autoplay fallbacks where relevant.
- Keep secrets out of code, logs, screenshots, summaries, widgets, and committed files.
- Prefer project-local tooling and existing scripts before adding dependencies. Explain any new dependency before installing it.
- End with a concise handoff: changed files, commands run, checks passed, checks not run, deployment URL if any, and next risks.
