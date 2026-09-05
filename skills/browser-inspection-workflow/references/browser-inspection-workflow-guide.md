# Browser Inspection Workflow Guide

## Purpose

- Make rendered-browser inspection a default part of shipping frontend work.

## Discovery Questions

- What URL or local server should be inspected?
- Which pages, modals, menus, forms, media, and interactions are critical?
- What browser/device sizes matter?
- Which errors are known versus new?

## Implementation Rules

- Inspect rendered output after substantial UI changes.
- Check console and failed requests.
- Test links/buttons/forms, not just static appearance.
- Use screenshots for visual claims.
- Warm lazy and reveal-heavy pages by scrolling through them before final captures.
- Reject native full-page screenshots that disagree with settled viewport behavior; use the stitched workflow in `$visual-regression-lab`.
- Report what was not inspectable.

## Useful Patterns

- Local dev server plus Playwright/Chrome inspection.
- Desktop and mobile smoke path through homepage, nav, CTA, form.
- Console/network capture before final answer.
- Screenshot proof for hero, mid-page, and mobile menu.
- Settled viewport stitching for Framer, WebGL, lazy media, pinned scenes, or scroll-reveal pages when one-shot full-page capture fails.

## Anti-Patterns

- Final says polished without opening the site.
- Console errors ignored.
- Only source code reviewed.
- Mobile nav or form never clicked.

## QA Checklist

- Open page, wait for assets, inspect console/network.
- Interact with nav, CTAs, forms, and media.
- Capture screenshots at key viewports.
- Fix or report visible defects.

## Acceptance Criteria

- Rendered browser behavior matches the intended design.
- Console/network issues are fixed or documented.
- The final report reflects actual inspection.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- Playwright screenshots: https://playwright.dev/docs/screenshots
- Playwright visual comparisons: https://playwright.dev/docs/test-snapshots
- Playwright emulation: https://playwright.dev/docs/emulation
- web.dev Web Vitals: https://web.dev/articles/vitals
- MDN Performance API: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
