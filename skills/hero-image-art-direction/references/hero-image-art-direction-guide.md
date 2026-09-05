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

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- MDN img element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img
- MDN picture element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- Next.js image optimization: https://nextjs.org/docs/app/getting-started/images
