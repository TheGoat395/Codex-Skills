# Animation Jank QA Guide

## Purpose

- Make motion feel intentional, smooth, and respectful instead of fragile.

## Discovery Questions

- What motion is essential versus decorative?
- Which animations run on scroll, route change, hover, or load?
- How does reduced motion behave?
- Are transforms/opacity used instead of expensive layout changes?

## Implementation Rules

- Respect prefers-reduced-motion.
- Avoid scroll traps and mobile pinning dead zones.
- Prefer transform/opacity for frequent motion.
- Clean up timelines/listeners on route changes.
- Test rapid scroll and resize.

## Useful Patterns

- Reduced-motion static equivalent.
- ScrollTrigger refresh after images load.
- Hover/focus parity for important states.
- Performance pass for long-running loops.

## Anti-Patterns

- Motion hides content or blocks navigation.
- Pinned mobile section creates blank scroll.
- Infinite animation drains CPU.
- Reduced motion ignored.

## QA Checklist

- Inspect desktop/mobile scroll and resize.
- Toggle reduced motion if possible.
- Check console and performance symptoms.
- Verify route cleanup in SPA/Next apps.

## Acceptance Criteria

- Motion supports hierarchy and interaction.
- No obvious jank, scroll traps, or broken reduced-motion path remains.
- Animation risk is documented.

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.

## Official Source Anchors

- web.dev Web Vitals: https://web.dev/articles/vitals
- MDN Performance API: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
- Playwright screenshots: https://playwright.dev/docs/screenshots
- Playwright visual comparisons: https://playwright.dev/docs/test-snapshots
- Playwright emulation: https://playwright.dev/docs/emulation
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
