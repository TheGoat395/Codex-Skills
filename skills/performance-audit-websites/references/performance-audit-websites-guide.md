# Performance Audit Websites Guide

## Purpose

- Keep premium sites fast enough that visual ambition does not punish users.

## Discovery Questions

- What is likely the LCP element?
- What scripts, media, fonts, and third parties dominate load?
- Where can layout shift or long tasks occur?
- Are lab and field metrics both relevant?

## Implementation Rules

- Prioritize the actual first viewport and LCP media.
- Reserve space for media and dynamic content.
- Do not add heavy libraries for small effects.
- Reduce third-party and animation cost.
- Report lab-only limits honestly.

## Useful Patterns

- Network asset inventory.
- LCP image/font/preload check.
- CLS check for images, embeds, cookie bars, and dynamic sections.
- Runtime interaction check for menus/forms/animations.

## Anti-Patterns

- Beautiful video hero with no poster and huge transfer.
- Images without dimensions.
- Several animation libraries for tiny effects.
- Performance score claimed without running tools.

## QA Checklist

- Run available build and performance tooling.
- Inspect network transfer and console warnings.
- Check Core Web Vitals risks.
- Document measured versus inferred findings.

## Acceptance Criteria

- Major performance risks are identified and reduced.
- Media and layout stability are handled.
- Performance claims are evidence-backed.

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
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- MDN video element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video
