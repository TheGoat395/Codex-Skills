# Image Video Loading QA Guide

## Purpose

- Make media-rich sites look intentional instead of broken, cropped, or slow.

## Discovery Questions

- Which media is critical above the fold?
- Do images/video have dimensions, poster, preload/lazy strategy, and fallbacks?
- Are responsive crops correct?
- Are alt/captions/transcripts needed?

## Implementation Rules

- Do not ship broken image/video requests.
- Reserve layout space for media.
- Provide poster frames for videos.
- Use meaningful alt/captions for informative media.
- Inspect mobile crops before final.

## Useful Patterns

- Hero image LCP priority and responsive sizes check.
- Video: poster, muted/playsinline/autoplay behavior, reduced-motion fallback.
- Gallery: lazy loading, stable tile aspect ratios, no 404s.
- CMS media: missing/empty asset fallback.

## Anti-Patterns

- Video hero flashes black with no poster.
- Mobile crop removes product/person/venue.
- Huge original image used as thumbnail.
- Alt text is missing or generic.

## QA Checklist

- Inspect network for 404s and oversized media.
- Capture desktop/mobile screenshots.
- Check dimensions, object-position, poster, and fallback.
- Test reduced motion where relevant.

## Acceptance Criteria

- Critical media loads, frames, and falls back correctly.
- No obvious media 404s or layout jumps remain.
- Media accessibility is handled.

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

- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- MDN video element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video
- web.dev Web Vitals: https://web.dev/articles/vitals
- MDN Performance API: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
