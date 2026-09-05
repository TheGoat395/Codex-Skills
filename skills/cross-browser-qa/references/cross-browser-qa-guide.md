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

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- Playwright screenshots: https://playwright.dev/docs/screenshots
- Playwright visual comparisons: https://playwright.dev/docs/test-snapshots
- Playwright emulation: https://playwright.dev/docs/emulation
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- MDN video element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
