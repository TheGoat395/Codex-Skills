# React Error Loading Empty States Guide

## Purpose

Prevent premium interfaces from collapsing into raw errors or empty blank boxes.

## Use When

- A component fetches or depends on async data.
- A list, gallery, dashboard, cart, search, form, or route can be empty, loading, errored, or not found.
- The site needs professional UX polish beyond the happy path.

## Do Not Use When

- The component is static and cannot meaningfully fail or be empty.
- The project has a complete fallback design system and this task does not touch it.
- The user asks only for backend error handling with no UI surface.

## Discovery Questions

- What states exist: initial, loading, refreshing, empty, partial, error, offline, not-found, success?
- Can the user recover: retry, clear filters, go back, contact support, browse related content?
- Should the state be route-level or component-level?
- How does the fallback preserve the site's visual direction?

## Decision Tree

- For route-level states in Next.js, use scoped loading/error/not-found files where appropriate.
- For component-level async UI, use Suspense or local state patterns that fit the data layer.
- Design skeletons only when shape helps; otherwise use concise status panels.
- Make empty states specific to the user action that caused them.
- Provide retry or recovery where possible.

## Implementation Rules

- Do not ship raw stack traces, default browser errors, or blank empty regions.
- Avoid skeletons that look like generic gray bars unrelated to the final layout.
- Keep copy calm, specific, and actionable.
- Preserve layout dimensions to avoid jarring shifts.
- Log or surface diagnostic detail only where appropriate for the audience.

## Useful Patterns

- Portfolio no project: curated fallback with link to index or contact.
- Commerce empty cart: product recommendations and clear continue-shopping action.
- Dashboard empty chart: explain missing data and show setup action.

## Anti-Patterns

- An empty state that says Nothing here.
- Spinners that replace everything and never explain progress.
- Error copy that blames the user or leaks internals.
- Loading states with different layout from final content causing large shifts.

## QA Checklist

- Force empty data, error data, slow data, and not-found routes if feasible.
- Test retry and clear-filter flows.
- Check mobile layout and text wrapping in fallback states.
- Verify focus and screen-reader announcements for important errors.

## Acceptance Criteria

- Every non-happy path feels intentionally designed.
- Users know what happened and what they can do next.
- Fallbacks match the quality of the main interface.

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.

## Official Source Anchors

- App Router layouts and pages: https://nextjs.org/docs/app/getting-started/layouts-and-pages
- React Learn: https://react.dev/learn
- React reference: https://react.dev/reference/react

## Scoped recovery

Cover the states affected by the request. Preserve useful existing data during background refresh, entered values across retryable failures and predictable focus/announcements during recovery. Do not clear the whole page or redesign unrelated states to repair one fallback. Test the actual retry outcome and interrupted/stale requests when relevant.
