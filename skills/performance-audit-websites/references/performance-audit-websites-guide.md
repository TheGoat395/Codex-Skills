# Performance Audit Websites Guide

## Purpose

- Keep premium sites fast enough that visual ambition does not punish users.

## Discovery Questions

- What is likely the LCP element?
- What scripts, media, fonts, and third parties dominate load?
- Where can layout shift or long tasks occur?
- Are lab and field metrics both relevant?

## Implementation Rules

- Establish a baseline before changing implementation and rerun the same measurement afterward.
- Prioritize the actual first viewport and LCP media.
- Reserve space for media and dynamic content.
- Do not add heavy libraries for small effects.
- Reduce third-party and animation cost.
- For React or Next.js, inspect waterfalls, server/client boundaries, serialized props, route-level loading, and initial JavaScript before micro-optimizing component code.
- Report lab-only limits honestly.

## Useful Patterns

- Network asset inventory.
- LCP image/font/preload check.
- CLS check for images, embeds, cookie bars, and dynamic sections.
- Runtime interaction check for menus/forms/animations.
- Route/server timing plus bundle inspection for React/Next.js work.

## Anti-Patterns

- Beautiful video hero with no poster and huge transfer.
- Images without dimensions.
- Several animation libraries for tiny effects.
- Performance score claimed without running tools.

## QA Checklist

- Run available build and performance tooling.
- Inspect network transfer and console warnings.
- Check Core Web Vitals risks.
- Document measured versus inferred findings.

## Acceptance Criteria

- Major performance risks are identified and reduced.
- Media and layout stability are handled.
- The same relevant measurement is compared before and after a claimed optimization.
- Performance claims are evidence-backed.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- web.dev Web Vitals: https://web.dev/articles/vitals
- MDN Performance API: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- MDN video element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video
