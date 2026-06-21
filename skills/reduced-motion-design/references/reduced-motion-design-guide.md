# Reduced Motion Design Guide

## Purpose

Respect motion preferences while keeping the experience polished and understandable.

## Use When

- A site includes parallax, scroll-linked motion, page transitions, large scale/pan movement, pinned scenes, 3D motion, or gesture animation.
- The user asks for accessibility or reduced-motion support.
- A final motion QA pass is needed before delivery.

## Do Not Use When

- The UI has no motion beyond unavoidable browser default behavior.
- A separate accessibility audit is in progress and already covers this exact scope.
- The user explicitly asks for a conceptual explanation only.

## Discovery Questions

- Which animations are essential state feedback and which are decorative?
- Which movement types could trigger discomfort: scale, zoom, parallax, pan, vestibular movement, continuous motion?
- How does the project detect reduced motion?
- What still communicates hierarchy and state without motion?

## Decision Tree

- Identify large, continuous, scroll-linked, or spatial motion first.
- Replace non-essential motion with instant state, opacity, color, or layout changes.
- Keep necessary feedback such as focus, loading, and selection visible.
- Use CSS media queries and library hooks consistently.
- Test with reduced-motion emulation where possible.

## Implementation Rules

- Do not simply remove all feedback.
- Avoid scaling, zooming, and panning large objects for reduced-motion users.
- Disable or simplify parallax and scroll-scrubbed scenes.
- Keep page content and actions accessible without waiting for animation.
- Make reduced-motion behavior part of QA, not an afterthought.

## Useful Patterns

- Replace reveal y-movement with opacity or instant visible state.
- Replace page wipe with immediate route swap and focus management.
- Replace pinned scroll choreography with stacked static sections.
- Replace 3D camera motion with static product render or poster.

## Anti-Patterns

- No reduced-motion handling on a motion-heavy site.
- Turning off focus/loading feedback entirely.
- Leaving scroll-triggered transforms active because they are subtle.
- Testing only the default motion path.

## QA Checklist

- Enable reduced motion in browser/OS emulation when possible.
- Check page transitions, scroll scenes, hover/tap, video, and 3D.
- Verify content is visible and workflows remain clear.
- Report any motion that could not be tested.

## Acceptance Criteria

- Reduced-motion users receive a complete, polished experience.
- Essential state feedback remains visible.
- Motion-sensitive effects are removed, reduced, or replaced.

## Shared Website Requirements

- Inspect before coding: framework, router, rendering mode, styling system, motion libraries, scroll setup, entry files, reduced-motion handling, and available verification commands.
- Use the existing project motion stack first. Add Motion, GSAP, Lenis, or other animation libraries only when the interaction requires them and explain why.
- Prefer CSS transitions for simple local state changes; use Motion for React-state, layout, gesture, and component transitions; use GSAP for timeline-heavy, scroll-pinned, SVG, text, or advanced choreography.
- Keep animation purposeful: clarify sequence, depth, focus, tactility, or product understanding. Do not use motion to hide weak layout or generic copy.
- Respect accessibility: reduced motion, keyboard access, focus management, no hover-only essential behavior, and no motion that blocks content.
- Protect performance: prefer transform and opacity, avoid layout thrashing, clean up timelines/listeners/observers, and test mobile.
- Run available lint, build, test, and local browser checks when possible; report exact commands and untested areas.

## Official Source Anchors

- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
- Motion for React: https://motion.dev/docs/react
- Motion gestures: https://motion.dev/docs/react-gestures
