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

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
- Motion for React: https://motion.dev/docs/react
- Motion gestures: https://motion.dev/docs/react-gestures
