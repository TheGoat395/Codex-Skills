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

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- MDN video element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video
- web.dev Web Vitals: https://web.dev/articles/vitals
- MDN Performance API: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
