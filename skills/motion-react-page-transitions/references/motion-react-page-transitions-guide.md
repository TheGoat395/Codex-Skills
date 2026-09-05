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

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.

## Official Source Anchors

- Motion AnimatePresence: https://motion.dev/docs/react-animate-presence
- Motion layout animations: https://motion.dev/docs/react-layout-animations
- MDN View Transition API: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
- MDN prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
