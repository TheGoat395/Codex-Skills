# Animation Jank QA Guide

## Purpose

- Make motion feel intentional, smooth, and respectful instead of fragile.

## Discovery Questions

- What motion is essential versus decorative?
- Which animations run on scroll, route change, hover, or load?
- How does reduced motion behave?
- Are transforms/opacity used instead of expensive layout changes?

## Implementation Rules

- Respect prefers-reduced-motion.
- Avoid scroll traps and mobile pinning dead zones.
- Prefer transform/opacity for frequent motion.
- Clean up timelines/listeners on route changes.
- Test rapid scroll and resize.

## Useful Patterns

- Reduced-motion static equivalent.
- ScrollTrigger refresh after images load.
- Hover/focus parity for important states.
- Performance pass for long-running loops.

## Anti-Patterns

- Motion hides content or blocks navigation.
- Pinned mobile section creates blank scroll.
- Infinite animation drains CPU.
- Reduced motion ignored.

## QA Checklist

- Inspect desktop/mobile scroll and resize.
- Toggle reduced motion if possible.
- Check console and performance symptoms.
- Verify route cleanup in SPA/Next apps.

## Acceptance Criteria

- Motion supports hierarchy and interaction.
- No obvious jank, scroll traps, or broken reduced-motion path remains.
- Animation risk is documented.

## Shared Website Requirements

- Inspect before changing or shipping: framework, package scripts, build output, routes, forms, media, animation stack, deployment target, environment variables, analytics, SEO metadata, accessibility risks, and available browser QA tooling.
- Do not claim something was tested unless it was actually tested; report exact commands, URLs, screenshots, viewports, failures, skipped checks, and remaining risk.
- Verify desktop and mobile rendered output, not only source code. For visual or motion work, inspect screenshots, browser behavior, console errors, network failures, and responsive layout.
- Treat forms, checkout, booking, CMS content, analytics, environment variables, and deployments as production surfaces with error, loading, empty, success, and rollback states.
- Respect accessibility, performance, reduced-motion, and no-JavaScript/no-WebGL/no-autoplay fallbacks where relevant.
- Keep secrets out of code, logs, screenshots, summaries, widgets, and committed files.
- Prefer project-local tooling and existing scripts before adding dependencies. Explain any new dependency before installing it.
- End with a concise handoff: changed files, commands run, checks passed, checks not run, deployment URL if any, and next risks.

## Official Source Anchors

- web.dev Web Vitals: https://web.dev/articles/vitals
- MDN Performance API: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
- Playwright screenshots: https://playwright.dev/docs/screenshots
- Playwright visual comparisons: https://playwright.dev/docs/test-snapshots
- Playwright emulation: https://playwright.dev/docs/emulation
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
