---
name: visual-regression-lab
description: "Compare captures; stitch lazy/animated pages."
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

Read [baseline contract](references/baseline-contract.md). When a project has Playwright installed, run `node "<skill-root>/scripts/capture-settled-baseline.mjs" <url> <output-dir>` to capture settled desktop/mobile/reduced-motion states and a machine-readable inspection manifest.

When native full-page capture is blank, sparse, incomplete, or inconsistent with real scrolling, read [stitched full-page capture](references/stitched-full-page-capture.md) and run `node "<skill-root>/scripts/capture-stitched-full-page.mjs" --url <url> --output <image>`. Treat the stitched image as evidence only after visual inspection.

## Output

Report:

- routes/viewports checked
- screenshots or saved paths when available
- issues found and fixed
- commands run
- anything not tested

Resolve `<skill-root>` to this skill folder's actual absolute location; preserve project-local module resolution for Node capture tools.
