# Motion Performance QA Guide

## Purpose

Catch the animation issues that make a premium site feel fragile or slow.

## Use When

- Any visible motion or scroll choreography has changed.
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

## Shared Website Requirements

- Inspect before coding: framework, router, rendering mode, styling system, motion libraries, scroll setup, entry files, reduced-motion handling, and available verification commands.
- Use the existing project motion stack first. Add Motion, GSAP, Lenis, or other animation libraries only when the interaction requires them and explain why.
- Prefer CSS transitions for simple local state changes; use Motion for React-state, layout, gesture, and component transitions; use GSAP for timeline-heavy, scroll-pinned, SVG, text, or advanced choreography.
- Keep animation purposeful: clarify sequence, depth, focus, tactility, or product understanding. Do not use motion to hide weak layout or generic copy.
- Respect accessibility: reduced motion, keyboard access, focus management, no hover-only essential behavior, and no motion that blocks content.
- Protect performance: prefer transform and opacity, avoid layout thrashing, clean up timelines/listeners/observers, and test mobile.
- Run available lint, build, test, and local browser checks when possible; report exact commands and untested areas.

## Official Source Anchors

- Motion for React: https://motion.dev/docs/react
- GSAP ScrollTrigger: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- Lenis GitHub README: https://github.com/darkroomengineering/lenis
- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
