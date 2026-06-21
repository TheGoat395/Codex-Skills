# UI Screenshot Composition Guide

## Purpose

- Turn UI screenshots into a designed evidence system, not a pile of framed rectangles.

## Use When

- A page has multiple screenshots that need hierarchy and rhythm.
- Feature sections feel like generic card grids with tiny UI images.
- Screenshots need responsive crop, annotation, zoom, or comparison treatment.

## Do Not Use When

- There are no UI screenshots or product visuals.
- A single raw screenshot is already the clearest proof.
- The task is only capturing new screenshots, not composing them.

## Discovery Questions

- Which screenshot is primary proof and which are supporting details?
- What should be visible at first glance versus on hover/zoom?
- Do annotations help, or do they clutter?
- How should screenshots crop or stack on mobile?

## Decision Tree

- Rank screenshots by evidence value.
- Use scale contrast: one dominant proof, smaller detail crops, concise callouts.
- Keep annotations outside important UI when possible.
- Use consistent frames, radii, shadows, and backgrounds.
- Test mobile stack for readability and overflow.

## Implementation Rules

- Do not create endless screenshot cards with equal weight.
- Avoid annotations that cover the UI they explain.
- Do not use heavy 3D transforms on text-heavy screenshots.
- Keep screenshots aligned to section copy and CTA intent.
- Use real screenshots or honest prototypes, not random generated UI.

## Useful Patterns

- One large workflow screenshot plus two magnified detail crops.
- Before/after comparison with consistent viewport and labels.
- Stacked dashboard cards with one highlighted metric and supporting table crop.
- Mobile-first product proof with phone screenshot and surrounding benefit copy.

## Anti-Patterns

- Every feature gets the same small rounded card.
- Screenshot wall has no focal point.
- UI is angled until unreadable.
- Callout lines, dots, and labels overwhelm the product.

## QA Checklist

- Inspect screenshot readability and focal hierarchy.
- Check mobile crop, overflow, and touch targets for zoom/detail views.
- Verify alt text/captions for informative screenshots.
- Run browser checks for asset loading and layout shift.

## Acceptance Criteria

- Screenshot composition creates clear product proof.
- Visual rhythm feels intentional and premium.
- Users can read the important UI at target viewports.

## Shared Website Requirements

- Inspect before coding: framework, image/video components, asset folders, CMS or source content, styling system, responsive breakpoints, performance checks, accessibility checks, and available browser QA commands.
- Treat images and video as content strategy, not decoration: every asset should reveal the real product, person, venue, object, interface, proof, or mood needed by the page.
- Avoid generic stock-like visuals, dark blurred filler, random gradients, and media that crops away the subject users need to inspect.
- Plan desktop, mobile, high-density, slow-network, reduced-motion, no-autoplay, failed-asset, and screen-reader states.
- Reserve layout space with dimensions, aspect-ratio, CSS constraints, or framework image components to avoid layout shift.
- Use meaningful alt text for informative images, empty alt for decorative images, captions/transcripts/tracks for media that needs them, and visible text for critical information.
- Before delivery, inspect rendered desktop and mobile media crops, verify assets load without 404s, and run available lint/build/test/browser checks.

## Official Source Anchors

- MDN img element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- Next.js image optimization: https://nextjs.org/docs/app/getting-started/images
- W3C WAI alt decision tree: https://www.w3.org/WAI/tutorials/images/decision-tree/
