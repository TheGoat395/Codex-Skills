# Native React View Transitions

## Scope

Use this reference when a React or Next.js app needs native view transitions for route changes, shared elements, Suspense reveals, list identity, or in-page state changes. Verify the installed React and framework versions before relying on an API that may still be experimental in that environment.

## Activation contract

- Render React's `<ViewTransition>` around the smallest meaningful boundary.
- Trigger the state change inside `startTransition`, `useDeferredValue`, or a Suspense reveal. A normal synchronous `setState` does not activate a React view transition.
- For enter and exit behavior, place the boundary before the DOM it owns. An extra wrapper that renders first can suppress the boundary's enter or exit capture.
- Do not call `document.startViewTransition` yourself when React owns the transition lifecycle.
- Keep content correct when transitions are unsupported. The browser should still receive the same semantic DOM and interaction path.

## Choose the relationship first

| Situation | Use | Meaning |
|---|---|---|
| List item becomes a detail view | Shared `name` | The same object is becoming more detailed |
| Data replaces a loading fallback | `enter` and `exit` | Content has arrived |
| Items reorder or filter | Stable keyed boundaries | These are the same items in a new arrangement |
| A panel appears or disappears | `enter` and `exit` | State changed locally |
| A route has real spatial depth | Typed page enter/exit | The reader moved forward or backward |

Do not add a route slide when the navigation is lateral and has no spatial relationship. A fade or no transition is more honest for tabs and unrelated destinations.

## Shared elements and names

Use one unique name for the outgoing and incoming instance that represent the same object. Include an ID when a list can show more than one object. Only one mounted boundary may own a given name at a time.

If the name participates in a type-keyed `share` map, every navigation path that should morph must provide the matching transition type. Plain links, browser back, and `router.back()` may not carry that type, so their default behavior must remain usable.

Give text that changes size substantially a text-specific treatment instead of relying on raster scaling. Never pair an outgoing shared-element morph with an unrelated full-page fade that dissolves the source object.

## Defaults and triggers

Use `default="none"` for named or type-keyed boundaries when an automatic cross-fade would be misleading. Opt into only the `enter`, `exit`, `share`, or `update` behavior that the boundary owns. Leave keyed list items and direct siblings that need displacement morphs eligible for updates.

Keep navigation types on page-level boundaries. Suspense resolves in a later transition without navigation types, so use plain string enter/exit classes for loading-to-content reveals.

## React and Next.js details

- In Next.js App Router, confirm the installed runtime exposes the React API before adding it. Do not install a canary solely because a guide mentions one.
- `transitionTypes` on supported links can carry navigation intent without turning a server component into a client component. `addTransitionType`, client router helpers, and `startTransition` require the appropriate client boundary.
- Browser history traversal may not carry directional types. Preserve a sensible default and test back, forward, refresh, and direct loads.
- Avoid wrapping an entire layout in a parent transition when nested page boundaries need their own enter/exit lifecycle.

## Accessibility and performance

- Provide a reduced-motion rule that disables or shortens the animation while keeping state and content changes immediate.
- Keep transitions short enough that scrolling, focus movement, and keyboard activation are not blocked.
- Use transform and opacity for custom CSS effects; do not animate layout properties without a measured reason.
- Keep focus, scroll position, loading states, and error paths explicit. A transition is not a replacement for navigation or feedback.
- Portal or isolate persistent chrome and floating controls when the root snapshot would otherwise make them flicker. Test hit testing during the transition.

## Verification checklist

1. Confirm the target runtime and browser support matrix.
2. Exercise the changed path with a keyboard and a screen reader-friendly DOM.
3. Test first load, client navigation, browser back/forward, refresh, deep links, and failure states.
4. Test shared names with two adjacent items to catch collisions.
5. Test loading and Suspense reveals separately from route transitions.
6. Test narrow viewports and reduced-motion settings.
7. Inspect console errors, focus movement, scroll behavior, and visual overlap.

## Sources

- https://react.dev/reference/react/ViewTransition
- https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
- https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md
