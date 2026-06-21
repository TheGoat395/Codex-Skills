# Cross Browser QA Guide

## Purpose

- Catch browser-specific issues that one local Chromium pass will miss.

## Discovery Questions

- Which browsers and platforms matter for the audience?
- What features are browser-sensitive: video autoplay, CSS, forms, canvas, sticky, scroll, fonts?
- Can Playwright projects or manual browsers cover the risk?
- What is acceptable fallback?

## Implementation Rules

- At least smoke-test core pages and conversion paths across available engines when risk warrants.
- Do not assume Safari/WebKit video and sticky behavior matches Chromium.
- Check forms/focus and media behavior.
- Document browsers not tested.
- Avoid unsupported CSS without fallback.

## Useful Patterns

- Chromium/WebKit/Firefox smoke for homepage, nav, form, media.
- Safari-like mobile video and sticky header check.
- Firefox layout/font check.
- Canvas/WebGL fallback check.

## Anti-Patterns

- Only Chrome tested for a video-heavy site.
- Browser-specific CSS warning ignored.
- WebKit mobile menu broken.
- Fallback not defined.

## QA Checklist

- Run Playwright projects if configured.
- Capture screenshots or notes by browser.
- Check console/network errors.
- Report unavailable browser coverage.

## Acceptance Criteria

- Critical paths work in targeted browsers or risks are explicit.
- Browser-specific layout/media bugs are fixed.
- Fallbacks are intentional.

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

- Playwright screenshots: https://playwright.dev/docs/screenshots
- Playwright visual comparisons: https://playwright.dev/docs/test-snapshots
- Playwright emulation: https://playwright.dev/docs/emulation
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- MDN video element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
