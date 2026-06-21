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
- Browser inspection is impossible and the user only wants code review.

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
- MDN picture element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- Next.js image optimization: https://nextjs.org/docs/app/getting-started/images
- web.dev image performance: https://web.dev/learn/performance/image-performance
