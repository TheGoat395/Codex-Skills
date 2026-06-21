# Motion React Layout Transitions Guide

## Purpose

Animate layout changes in a way that clarifies continuity instead of causing jumpy UI.

## Use When

- A component changes size, position, order, selected state, or layout in response to React state.
- Shared element continuity would make a product UI, portfolio, gallery, nav underline, or tab set feel polished.
- The project uses Motion and layout changes currently snap awkwardly.

## Do Not Use When

- The animation is only a route-level page transition.
- The layout change is better expressed with instant state for speed or accessibility.
- A browser View Transition or GSAP timeline is the established local pattern.

## Discovery Questions

- Which element should visually persist between states?
- Does the transition need `layout`, `layoutId`, or a `LayoutGroup`?
- What should happen to focus and scroll during the layout change?
- Does the layout animation distort children, images, borders, or shadows?

## Decision Tree

- Use `layout` for a single element's size/position changes.
- Use `layoutId` for shared element transitions between components.
- Use `LayoutGroup` when related elements need coordinated measurement.
- Prefer transform-based layout animation and avoid animating raw width/height manually.
- Disable or simplify layout motion when reduced motion is requested.

## Implementation Rules

- Animate continuity only where users benefit from understanding what moved.
- Avoid shared element transitions between visually unrelated objects.
- Preserve semantic DOM order and keyboard flow.
- Keep stable keys for animated lists.
- Watch for clipping, z-index, border-radius distortion, and image stretching.

## Useful Patterns

- Active nav underline with `layoutId`.
- Portfolio grid card expands into a preview panel.
- Filter chips reorder with subtle layout motion.
- Product UI pane shifts between summary and detail while preserving context.

## Anti-Patterns

- Layout animations on every list item in a dense dashboard.
- Missing keys causing components to animate as the wrong object.
- Huge springy movement on serious or luxury UI.
- Animating layout without testing mobile wraps.

## QA Checklist

- Test repeated open/close, filter, reorder, and resize.
- Check mobile, reduced motion, and keyboard focus.
- Inspect z-index and clipping during transition.
- Run build/lint to catch React key and import issues.

## Acceptance Criteria

- Layout motion improves orientation and feels physically plausible.
- No content jumps, overlaps, or distorts during transitions.
- The implementation remains accessible and maintainable.

## Shared Website Requirements

- Inspect before coding: framework, router, rendering mode, styling system, motion libraries, scroll setup, entry files, reduced-motion handling, and available verification commands.
- Use the existing project motion stack first. Add Motion, GSAP, Lenis, or other animation libraries only when the interaction requires them and explain why.
- Prefer CSS transitions for simple local state changes; use Motion for React-state, layout, gesture, and component transitions; use GSAP for timeline-heavy, scroll-pinned, SVG, text, or advanced choreography.
- Keep animation purposeful: clarify sequence, depth, focus, tactility, or product understanding. Do not use motion to hide weak layout or generic copy.
- Respect accessibility: reduced motion, keyboard access, focus management, no hover-only essential behavior, and no motion that blocks content.
- Protect performance: prefer transform and opacity, avoid layout thrashing, clean up timelines/listeners/observers, and test mobile.
- Run available lint, build, test, and local browser checks when possible; report exact commands and untested areas.

## Official Source Anchors

- Motion layout animations: https://motion.dev/docs/react-layout-animations
- Motion for React: https://motion.dev/docs/react
- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
