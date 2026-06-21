---
name: web-imagegen-prompting
description: "Prompt generated imagery for premium websites. Use when Codex needs hero images, product scenes, editorial visuals, backgrounds, portraits, venue imagery, campaign art, texture assets, mockups, or image-generation direction for luxury, cinematic, Squarespace-polished, Viktor Oddy-adjacent, or non-generic site visuals."
---

# Web Imagegen Prompting

Use this skill to make generated imagery usable as website media instead of vague atmospheric filler.

## Workflow

1. Inspect the project, media assets, framework image/video APIs, responsive breakpoints, accessibility requirements, and verification commands.
2. Read [Web Imagegen Prompting Guide](references/web-imagegen-prompting-guide.md) for detailed direction before changing visuals or code.
3. Define the media's job: proof, desire, navigation, instruction, atmosphere, conversion, or accessibility.
4. Implement with stable dimensions, responsive crops, useful fallbacks, and real content hierarchy.
5. Inspect rendered desktop and mobile states, then refine crop, contrast, loading, labels, captions, and polish.

## Always Protect

- Inspect before coding: framework, image/video components, asset folders, CMS or source content, styling system, responsive breakpoints, performance checks, accessibility checks, and available browser QA commands.
- Treat images and video as content strategy, not decoration: every asset should reveal the real product, person, venue, object, interface, proof, or mood needed by the page.
- Avoid generic stock-like visuals, dark blurred filler, random gradients, and media that crops away the subject users need to inspect.
- Plan desktop, mobile, high-density, slow-network, reduced-motion, no-autoplay, failed-asset, and screen-reader states.
- Reserve layout space with dimensions, aspect-ratio, CSS constraints, or framework image components to avoid layout shift.
- Use meaningful alt text for informative images, empty alt for decorative images, captions/transcripts/tracks for media that needs them, and visible text for critical information.
- Before delivery, inspect rendered desktop and mobile media crops, verify assets load without 404s, and run available lint/build/test/browser checks.
