---
name: visual-regression-lab
description: "Use after frontend changes or before delivery to run rendered visual QA with Playwright/browser screenshots, viewport checks, console/network checks, overflow detection, canvas/media verification, before/after comparisons, and responsive polish review."
---

# Visual Regression Lab

Use this skill to prove the site looks right in a browser, not just in code.

## Required Checks

1. Start or identify the local server.
2. Open the relevant route in a browser or Playwright.
3. Capture desktop and mobile screenshots.
4. Check console errors, failed requests, layout overflow, missing media, and text clipping.
5. Inspect first viewport composition, hierarchy, spacing, typography, image crops, and CTA visibility.
6. Test key interactions: nav, forms, menus, tabs, accordions, hover states, focus states, and modals.
7. For animation-heavy work, test reduced-motion behavior and watch for jank.
8. For canvas/WebGL/video, verify nonblank rendered pixels and stable framing.
9. Do one second-pass polish edit when the result feels generic or cramped.

## Output

Report:

- routes/viewports checked
- screenshots or saved paths when available
- issues found and fixed
- commands run
- anything not tested
