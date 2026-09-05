# Mobile Responsive QA Guide

## Purpose

- Catch mobile problems that make otherwise premium sites feel rushed.

## Discovery Questions

- Which phone/tablet sizes should be tested?
- What must remain visible in the first viewport?
- Which media crops, menus, forms, and tables are risky?
- Are touch targets and sticky actions comfortable?

## Implementation Rules

- Test real mobile-width screenshots, not only responsive CSS guesses.
- Check horizontal overflow and text wrapping.
- Verify mobile menu, sticky CTA, forms, tables, and galleries.
- Use separate mobile crops when desktop art direction fails.
- Report untested mobile states.

## Useful Patterns

- 390px phone, 768px tablet, 1440px desktop smoke set.
- Mobile menu open/close/focus screenshot.
- Pricing/table reflow check.
- Hero crop and first-action check.

## Anti-Patterns

- Desktop design simply stacks into a dull mobile page.
- Text overlaps or buttons truncate.
- Hero image crop loses subject.
- Tables overflow off-screen.

## QA Checklist

- Measure scrollWidth versus viewport.
- Capture mobile screenshots.
- Click menus/forms/CTAs.
- Inspect media crops and text wrapping.

## Acceptance Criteria

- Mobile layout is composed, readable, and actionable.
- No incoherent overlap or unintended horizontal scroll remains.
- Critical flows work on touch-sized screens.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- Playwright screenshots: https://playwright.dev/docs/screenshots
- Playwright visual comparisons: https://playwright.dev/docs/test-snapshots
- Playwright emulation: https://playwright.dev/docs/emulation
- MDN responsive images: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- MDN video element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
