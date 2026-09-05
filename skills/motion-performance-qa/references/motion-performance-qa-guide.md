# Motion Performance QA Guide

## Purpose

Catch the animation issues that make a premium site feel fragile or slow.

## Use When

- A substantial motion-system change or pre-delivery motion review needs broad lifecycle/performance coverage.
- A site uses Motion, GSAP, Lenis, WebGL, observers, timers, or custom RAF loops.
- The user expects high-end animation quality before final delivery.

## Do Not Use When

- No visible motion or interaction changed.
- The user asks only for backend/non-UI work.
- A code review stance is requested and design QA is out of scope.

## Discovery Questions

- Which animations, scroll scenes, and interactions changed?
- What devices and viewports are most important?
- What cleanup paths exist on route change and unmount?
- What reduced-motion behavior should be verified?

## Decision Tree

- Run automated checks first when available.
- Visually inspect desktop and mobile interaction paths.
- Test reduced motion, route changes, resize, rapid scroll, and repeated open/close.
- Inspect for layout shift, dropped frames, duplicate timelines, and stale listeners.
- Report exactly what was checked and what could not be checked.

## Implementation Rules

- Do not ship motion that was never viewed.
- Prefer transform and opacity; avoid layout thrashing.
- Kill timelines, listeners, observers, RAF loops, and timeouts on cleanup.
- Check mobile performance, not just desktop.
- Animation should never block content access or core workflow.

## Useful Patterns

- Motion audit: mount, hover/tap/focus, exit, reduced motion, route unmount.
- GSAP audit: context/revert, ScrollTrigger kill/refresh, pin positions, resize.
- Lenis audit: anchors, modals, nested scroll, route reset, duplicate RAF.
- WebGL audit: nonblank canvas, FPS feel, fallback, resource disposal.

## Anti-Patterns

- Final answer says polished without browser inspection.
- Animations duplicate after navigating back.
- Reduced-motion mode still has parallax and page wipes.
- Pinned scenes break after image load or resize.

## QA Checklist

- Check desktop, mobile, reduced motion, resize, and route navigation.
- Use screenshots, browser dev tools, or direct visual inspection when possible.
- Inspect console warnings/errors.
- Run lint/build/test commands available in the project.

## Acceptance Criteria

- Motion is smooth, accessible, cleaned up, and verified.
- Known risks or untested paths are honestly reported.
- The site feels premium because motion supports the experience.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- Motion for React: https://motion.dev/docs/react
- GSAP ScrollTrigger: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- Lenis GitHub README: https://github.com/darkroomengineering/lenis
- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
