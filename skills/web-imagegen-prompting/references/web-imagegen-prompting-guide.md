# Web Imagegen Prompting Guide

## Purpose

- Make generated imagery usable as website media instead of vague atmospheric filler.

## Use When

- The project lacks strong visual assets and generated imagery is acceptable.
- A hero, product, venue, portrait, texture, or editorial media system needs art direction.
- The current AI image prompt creates generic, unusable, cropped, or low-specificity visuals.

## Do Not Use When

- Real product, person, venue, legal, medical, or portfolio evidence must be shown accurately.
- The user has supplied brand-approved assets that should be used instead.
- The page can be stronger with typography, layout, or real screenshots rather than generated imagery.

## Discovery Questions

- What should the image prove or reveal on the page?
- What is the subject, setting, material, camera angle, crop, lighting, and mood?
- Which viewport crops must work: wide desktop, laptop, tablet, mobile, social preview?
- What must not appear: fake logos, incorrect product details, text in image, extra hands, stock-photo cues?

## Decision Tree

- Define the asset role before writing a prompt.
- Name subject, setting, camera, lens feel, lighting, material, composition, palette, and negative constraints.
- Request enough margin around the subject for responsive cropping.
- Generate variants by direction, not random style words.
- Inspect the output in the actual layout before accepting it.

## Implementation Rules

- Do not use vague words like premium or cinematic without specifying visible choices.
- Avoid text, logos, UI labels, or exact product details inside generated images unless they can be corrected.
- Prefer real screenshots, real photography, or supplied assets for factual proof.
- Make the image composition serve the page hierarchy and text placement.
- Keep prompts brand-specific and avoid generic stock-photo language.

## Useful Patterns

- Hero prompt with subject left/right negative space for overlaid type.
- Texture prompt for subtle material surface, not attention-grabbing decoration.
- Portrait prompt with environmental context and editorial crop.
- Product scene prompt with real usage context and inspectable object.

## Anti-Patterns

- Dark blurred background image with no subject.
- Generated luxury room that could belong to any brand.
- Image has text that looks broken or fake.
- Prompt asks only for 'modern premium cinematic website hero'.

## QA Checklist

- Place the image in the page and inspect desktop/mobile crops.
- Check for unwanted text, artifacts, distorted anatomy, fake UI, or wrong product details.
- Confirm contrast behind overlay text.
- Add accurate alt text or mark decorative as empty alt.

## Acceptance Criteria

- The generated asset has a clear subject and page role.
- It survives responsive cropping and supports readable typography.
- It feels specific to the brand/site rather than generic AI ambience.

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
- W3C WAI alt decision tree: https://www.w3.org/WAI/tutorials/images/decision-tree/
