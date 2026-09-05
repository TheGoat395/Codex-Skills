# React and Next.js performance

Use this reference for implementation or review in a React or Next.js codebase. Confirm the installed framework/version and current official documentation before using version-sensitive APIs.

## Prioritize by impact

1. **Eliminate avoidable waterfalls.** Start independent work together, defer awaits until their branch needs the result, and use Suspense/streaming where it improves the actual user path. Do not parallelize work with real data dependencies or ignore cancellation and error behavior.
2. **Reduce initial client JavaScript.** Keep server-renderable work on the server, place client boundaries around the smallest interactive islands, and avoid importing heavy modules through shared client entrypoints.
3. **Reduce server work and serialization.** Deduplicate request-scoped work, cache only with an explicit lifetime/invalidation model, parallelize independent data loading, and pass the minimum serializable data to clients.
4. **Control media, fonts, and third parties.** Prioritize real LCP assets, reserve dimensions, use responsive media, subset/preload fonts selectively, and defer noncritical third-party code.
5. **Optimize re-renders and JavaScript only when evidence points there.** Fix unnecessary state/effects and hot paths before adding memoization everywhere.

## Async and route work

- Start independent promises before awaiting them, then await at the latest safe point.
- Use `Promise.all` only when the work is independent and its failure semantics are acceptable.
- Place Suspense boundaries around meaningful user-visible units rather than every component.
- Avoid sequential fetches created accidentally by nested component structure.
- Make route loading, error, not-found, retry, and partial-content behavior explicit.

## Server/client boundaries

- Keep Server Components as the App Router default for data, content, secrets, and noninteractive composition.
- Add `use client` at the narrowest component that needs state, events, browser APIs, effects, or a client-only library.
- Inspect the entire imported client graph after moving a boundary; a tiny client file can pull in a large dependency tree.
- Pass small serializable props. Do not duplicate large objects through multiple RSC prop paths.
- Never keep request-specific mutable state at module scope.
- Authenticate Server Actions and handlers as external mutation surfaces.
- Use caching only when ownership, key, scope, invalidation, staleness, and failure behavior are defined.

## Bundle and loading

- Measure route chunks and initial JavaScript before claiming a bundle improvement.
- Prefer direct, statically analyzable imports when a package's documented export structure supports them; do not rewrite imports blindly when framework/package optimization already handles the case.
- Dynamically load genuinely heavy, noncritical client features. Preserve useful loading and error states.
- Load analytics, chat, and other third parties after critical rendering when the product requirement allows it.
- Preload only assets likely to be used soon; excessive preload competes with the real critical path.

## React rendering

- Derive render data during render; use Effects to synchronize with external systems, not to copy props into state.
- Keep transient high-frequency values out of render state when the UI does not need every update.
- Use transitions/deferred values for nonurgent expensive rendering where interaction measurements justify them.
- Avoid components defined inside components and unstable nonprimitive defaults that force remounts or invalidate memoization.
- Add memoization only around measured expensive work or a demonstrably unstable render path; memoization also has cost and complexity.
- Clean up listeners, observers, timers, animation instances, and subscriptions.

## Verification

Record the route, build mode, device/viewport, cache state, network/CPU conditions, tool/version, and timestamp. Compare like with like:

- production build output and route chunks;
- server timing and request waterfall;
- browser network and long tasks;
- LCP, CLS, and interaction behavior;
- hydration/console errors;
- desktop and representative mobile behavior.

Use field data when available and scoped correctly. Use lab data for reproducible diagnosis. Source inspection is evidence of a pattern, not proof of user impact.

Primary anchors:

- Vercel React best practices: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices
- React reference: https://react.dev/reference/react
- Next.js performance guidance: https://nextjs.org/docs/app/building-your-application/optimizing
- Next.js Server and Client Components: https://nextjs.org/docs/app/getting-started/server-and-client-components
