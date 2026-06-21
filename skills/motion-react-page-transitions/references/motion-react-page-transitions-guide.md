# Motion React Page Transitions Guide

## Purpose

Make route changes feel continuous while preserving speed, focus, direct URLs, and framework boundaries.

## Use When

- The user asks for Framer-like, cinematic, premium, Viktor-style, portfolio, or product page transitions.
- Route changes feel abrupt and a designed transition would improve orientation.
- A gallery, portfolio, product tour, or marketing site benefits from page-to-page continuity.

## Do Not Use When

- The site is an operational tool where instant navigation matters more than ceremony.
- The router/framework makes exit transitions fragile and there is no clear implementation path.
- The user has reduced-motion or accessibility constraints that rule out page motion.

## Discovery Questions

- Which router is used and where can client transition state safely live?
- Is this an exit/enter transition, shared element transition, loading transition, or native View Transition API case?
- How should focus and scroll position behave after navigation?
- What is the fast reduced-motion equivalent?

## Decision Tree

- Start with route loading, focus, scroll, and direct-load behavior.
- Use native View Transition API only where browser support and framework integration are acceptable.
- Use Motion/AnimatePresence when React component lifecycle can reliably hold exiting elements.
- Keep transition wrapper narrow and do not clientify the entire app unless required.
- Always provide a reduced-motion branch.

## Implementation Rules

- Do not block navigation behind long page wipes.
- Direct URL loads must render correctly without relying on prior route state.
- Focus should land predictably after navigation.
- Scroll reset/preservation must be explicit.
- Avoid global overlays that cover content if something fails.

## Useful Patterns

- Portfolio index to case study: shared thumbnail feel plus quick content fade.
- Product tour route: persistent shell with animated content region.
- Marketing page: subtle section transition and designed loading state.
- Reduced motion: instant content swap with opacity-only or no transition.

## Anti-Patterns

- Full-screen wipes on every nav click.
- Transition state that breaks browser back/forward.
- No direct-load fallback for detail pages.
- Over-clientifying server-rendered pages for a decorative transition.

## QA Checklist

- Test direct load, client navigation, back/forward, refresh, and mobile nav.
- Test reduced motion and keyboard focus.
- Check route loading and error states.
- Inspect console for unmounted animation errors.

## Acceptance Criteria

- Navigation remains fast, accessible, and reliable.
- Page motion feels site-specific and purposeful.
- The implementation fits the router and rendering model.

## Shared Website Requirements

- Inspect before coding: framework, router, rendering mode, styling system, motion libraries, scroll setup, entry files, reduced-motion handling, and available verification commands.
- Use the existing project motion stack first. Add Motion, GSAP, Lenis, or other animation libraries only when the interaction requires them and explain why.
- Prefer CSS transitions for simple local state changes; use Motion for React-state, layout, gesture, and component transitions; use GSAP for timeline-heavy, scroll-pinned, SVG, text, or advanced choreography.
- Keep animation purposeful: clarify sequence, depth, focus, tactility, or product understanding. Do not use motion to hide weak layout or generic copy.
- Respect accessibility: reduced motion, keyboard access, focus management, no hover-only essential behavior, and no motion that blocks content.
- Protect performance: prefer transform and opacity, avoid layout thrashing, clean up timelines/listeners/observers, and test mobile.
- Run available lint, build, test, and local browser checks when possible; report exact commands and untested areas.

## Official Source Anchors

- Motion AnimatePresence: https://motion.dev/docs/react-animate-presence
- Motion layout animations: https://motion.dev/docs/react-layout-animations
- MDN View Transition API: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
