# Native React View Transitions

## Scope

Use this reference when a React or Next.js app needs native view transitions for route changes, shared elements, Suspense reveals, list identity, or in-page state changes. React's `<ViewTransition>` component is currently documented for Canary and Experimental channels. Verify the installed React, framework, and browser versions before using it, and do not move a stable project to an experimental channel only because this guide mentions the API.

## Activation contract

- Render React's `<ViewTransition>` around the smallest meaningful boundary.
- Trigger the state change inside `startTransition`, `useDeferredValue`, or a Suspense reveal. A normal synchronous `setState` does not activate a React view transition.
- For enter and exit behavior, place the boundary before the DOM it owns. An extra wrapper that renders first can suppress the boundary's enter or exit capture.
- Do not call `document.startViewTransition` when React owns the lifecycle.
- Keep content correct when transitions are unsupported; the semantic DOM and interaction path must remain usable.

## Choose the relationship first

| Situation | Use | Meaning |
|---|---|---|
| List item becomes a detail view | Shared `name` | The same object becomes more detailed |
| Data replaces a loading fallback | `enter` and `exit` | Content has arrived |
| Items reorder or filter | Stable keyed boundaries | The same items moved |
| A panel appears or disappears | `enter` and `exit` | Local state changed |
| A route has real spatial depth | Typed page enter/exit | The reader moved forward or backward |

Do not add a route slide when navigation is lateral or unrelated. A fade or no transition is more honest for tabs and unrelated destinations.

## Shared elements and names

Use one unique name for outgoing and incoming instances of the same object. Include an ID when multiple objects may be mounted. Only one mounted boundary may own a given name at a time.

If a name participates in a type-keyed `share` map, every navigation path that should morph must provide the matching transition type. Plain links, browser back, and `router.back()` may not carry that type, so default behavior must remain usable.

Give text that changes size substantially a text-specific treatment instead of relying on raster scaling. Do not combine a shared-element morph with an unrelated full-page fade that dissolves its source.

## React and Next.js details

- In Next.js App Router, verify what the installed runtime actually exposes before adding React's component.
- `transitionTypes` on supported Next.js links can carry navigation intent. Client transition helpers still require an appropriate client boundary.
- Browser history traversal may not carry directional types. Test back, forward, refresh, and direct loads.
- Avoid wrapping an entire layout in a parent transition when nested page boundaries need independent enter and exit lifecycles.
- Next.js has described deeper View Transition integration as experimental; do not present it as a stable production guarantee.

## Accessibility and performance

- Provide a reduced-motion rule that disables or shortens animation without delaying state changes.
- Keep transitions short enough that scrolling, focus movement, and keyboard activation are not blocked.
- Prefer transform and opacity for custom effects; animate layout only with a measured reason.
- Keep focus, scroll position, loading states, and error paths explicit.
- Isolate persistent chrome when root snapshots make it flicker, then test hit testing during the transition.

## Verification checklist

1. Confirm runtime and browser support.
2. Test keyboard operation and semantic DOM behavior.
3. Test first load, client navigation, back and forward, refresh, deep links, and failures.
4. Test shared names with adjacent items to catch collisions.
5. Test loading and Suspense reveals separately from route transitions.
6. Test narrow viewports and reduced motion.
7. Inspect console errors, focus, scrolling, overlap, and interrupted navigation.

## Sources

- https://react.dev/reference/react/ViewTransition
- https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
- https://nextjs.org/blog/next-15-2
- https://nextjs.org/docs/app/api-reference/components/link#transitiontypes
