# Image Crop Responsive QA Guide

## Purpose

- Catch the crop, focal point, and layout bugs that make premium pages feel careless.

## Use When

- Any important image was added, replaced, resized, or art-directed.
- A layout uses object-fit, background-size, picture/source, responsive images, or framework Image components.
- The site needs a final visual polish pass for media.

## Do Not Use When

- No raster/vector images are present.
- The task is only server-side or data-layer work.
- No crop-related review is requested. Source-only review is allowed when browser inspection is unavailable; rendered crop conclusions remain unverified.

## Discovery Questions

- Which images are content-bearing and must keep a focal point visible?
- Which breakpoints/crops need separate assets or object-position?
- Are width/height/aspect-ratio/sizes specified correctly?
- Do lazy/priority/loading choices match above/below-the-fold placement?

## Decision Tree

- List critical images and their intended focal points.
- Inspect desktop, laptop, tablet, and mobile crops.
- Check dimensions, aspect ratio, sizes/srcset or framework image props.
- Verify lazy/priority/preload choices and no layout shift.
- Fix focal points, source art direction, or layout constraints before final.

## Implementation Rules

- Do not accept a hero crop until mobile is inspected.
- Do not lazy-load the critical LCP hero image without a reason.
- Do not omit dimensions or aspect-ratio from layout-critical images.
- Avoid background-image for meaningful content unless a semantic equivalent exists.
- Report when browser/screenshot QA could not be run.

## Useful Patterns

- Hero: desktop wide crop, mobile portrait crop, explicit focal object-position.
- Portrait grid: face-safe crops and consistent aspect ratios.
- Product gallery: stable tile dimensions and no product cutoffs.
- Screenshot section: separate mobile crop or zoomed detail image.

## Anti-Patterns

- Person face cropped out on mobile.
- Product grid jumps as images load.
- Huge original images used for tiny thumbnails.
- Image looks good only at one viewport width.

## QA Checklist

- Capture or inspect screenshots at common viewports.
- Check network for 404s and oversized assets.
- Inspect rendered image dimensions and object-position.
- Verify alt text for content-bearing images.

## Acceptance Criteria

- Critical images keep their focal point across breakpoints.
- Images load with stable layout and appropriate priority.
- The final page feels composed on mobile and desktop.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- MDN img element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img
- MDN picture element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- Next.js image optimization: https://nextjs.org/docs/app/getting-started/images
- web.dev image performance: https://web.dev/learn/performance/image-performance
