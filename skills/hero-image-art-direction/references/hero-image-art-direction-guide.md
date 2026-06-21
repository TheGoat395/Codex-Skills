# Hero Image Art Direction Guide

## Purpose

- Make the first viewport immediately specific, inspectable, and composed.

## Use When

- A page needs a hero image, video poster, visual background, or first-screen media choice.
- Current hero media is generic, too dark, too cropped, or fighting the typography.
- A mobile hero needs a different crop or asset from desktop.

## Do Not Use When

- The page is a dense app/tool where a hero is inappropriate.
- The user explicitly wants a text-only or data-first first viewport.
- The image is purely decorative and should be removed.

## Discovery Questions

- What should users understand in the first three seconds?
- Is the hero subject the product, place, person, work, interface, or atmosphere?
- Where can headline and controls sit without covering essential details?
- Do desktop and mobile need separate crops, art direction, or media files?

## Decision Tree

- Pick the subject and focal area before layout.
- Choose media with real inspectable content and enough quiet space for type.
- Define aspect ratio, object-position, and crop behavior per breakpoint.
- Tune overlay treatment only after image and type are placed.
- Verify first viewport and next-section hint on mobile and desktop.

## Implementation Rules

- Do not let overlay gradients hide weak or irrelevant imagery.
- Avoid split hero cards when an immersive media-first hero is expected.
- Do not crop faces, products, rooms, or UI details that carry meaning.
- Use a different mobile crop when the desktop composition fails.
- Keep text real HTML, not baked into the image.

## Useful Patterns

- Full-bleed venue image with low, quiet type zone and visible next section.
- Product close-up with strong silhouette and secondary proof nearby.
- Portfolio hero with one memorable work artifact, not a grid of thumbnails.
- Editorial portrait with environmental context and restrained overlay.

## Anti-Patterns

- Centered headline on a random unspecific background.
- Hero image cropped so the actual product is off-screen on mobile.
- Dark overlay used until the image no longer matters.
- Stock business photo with no connection to the offer.

## QA Checklist

- Inspect at desktop, laptop, tablet, and mobile widths.
- Check text contrast and focal point at each crop.
- Verify image loading, dimensions, and no layout shift.
- Confirm the first viewport shows the brand/product/place/person clearly.

## Acceptance Criteria

- The hero media carries the page concept immediately.
- Text, controls, and focal point coexist across viewports.
- The result feels composed rather than templated.

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
