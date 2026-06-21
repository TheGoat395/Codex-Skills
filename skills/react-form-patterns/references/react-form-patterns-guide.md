# React Form Patterns Guide

## Purpose

Make forms feel trustworthy and complete instead of unstyled utility afterthoughts.

## Use When

- A React or Next.js site needs any user input form.
- Fields need validation, loading, success, error, empty, disabled, or retry states.
- The user asks for checkout, booking, lead capture, signup, waitlist, inquiry, or newsletter functionality.

## Do Not Use When

- The form backend, action, or destination is unknown and the user only wants visual mockup.
- A form library and design system already define exact patterns.
- The task is unrelated to input or conversion.

## Discovery Questions

- What happens on submit: email, API, server action, payment, CRM, calendar, or placeholder?
- Which fields are required and why?
- What validation should happen client-side, server-side, or both?
- What should users see for loading, success, error, and resubmission?

## Decision Tree

- Start with semantic form, labels, field types, autocomplete, and accessible errors.
- Choose controlled state only when live validation, formatting, or dependent fields need it.
- Keep submit logic in submit handlers or server actions, not effect watchers.
- Design all states before finalizing layout.
- If backend is missing, isolate the submit adapter and make limitations explicit.

## Implementation Rules

- Never ship unlabeled fields or placeholder-only labels.
- Make errors specific, close to fields, and screen-reader accessible.
- Prevent double-submit with designed pending states.
- Use input types and autocomplete for mobile ergonomics.
- Do not fake a working form; state clearly if it is front-end only.

## Useful Patterns

- Luxury service inquiry: minimal fields, high-touch copy, confirmation state that sets expectations.
- Devtool waitlist: email plus role/company, clear privacy note, instant success feedback.
- Booking form: date/time/service selection, validation, summary, and recovery path.

## Anti-Patterns

- A beautiful page with a default browser form.
- Generic submit buttons like Submit when a more specific action exists.
- Validation only after a failed network request when simple client hints would help.
- Success state that disappears without telling the user what happens next.

## QA Checklist

- Submit empty, invalid, valid, and repeated submissions.
- Test keyboard and mobile input behavior.
- Check loading, disabled, success, and error states.
- Verify network/backend behavior or explicitly report if mocked.

## Acceptance Criteria

- The form is accessible, specific, and conversion-aware.
- Every submission state is designed.
- The implementation truthfully reflects backend availability.

## Shared Website Requirements

- Inspect before coding: project structure, framework, router, homepage or main entry, styling system, JavaScript or motion system, assets, and available commands.
- Prefer the existing project stack and conventions before adding dependencies or moving architecture.
- For Next.js App Router projects, keep Server Components as the default and introduce Client Components only for interactivity, browser APIs, effects, or client-only libraries.
- For React work, keep components pure, derive render data during render, and use Effects only to synchronize with external systems.
- Default website output must still follow the premium visual baseline: strong type, real content, designed states, responsive polish, and no generic card-grid filler.
- Run available lint, build, test, and local browser checks when possible; report exactly what ran and what was not tested.
- Check desktop and mobile behavior when changing visible UI, especially overflow, focus, loading, empty, error, and reduced-motion states.

## Official Source Anchors

- React reference: https://react.dev/reference/react
- You Might Not Need an Effect: https://react.dev/learn/you-might-not-need-an-effect
- Next.js docs overview: https://nextjs.org/docs
