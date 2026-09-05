# React Form Patterns Guide

## Purpose

Make forms feel trustworthy and complete instead of unstyled utility afterthoughts.

## Use When

- A React or Next.js site needs any user input form.
- Fields need validation, loading, success, error, empty, disabled, or retry states.
- The user asks for checkout, booking, lead capture, signup, waitlist, inquiry, or newsletter functionality.

## Do Not Use When

- The task has no form/input surface. A requested visual mockup remains in scope: provide real labels, semantics and state designs with an explicitly inactive or mocked submit adapter.
- Existing form behavior is correct and this request neither changes nor reviews it. Follow an established library/design pattern when implementing or repairing a form.
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

- Test empty, invalid, valid and repeated submissions through a local fixture, test route or authorized test destination. Never create a real payment, booking, message or client record merely to satisfy QA.
- Test keyboard and mobile input behavior.
- Check loading, disabled, success, and error states.
- Verify network/backend behavior or explicitly report if mocked.

## Acceptance Criteria

- The form is accessible, specific, and conversion-aware.
- Every submission state is designed.
- The implementation truthfully reflects backend availability.

## Shared scope

For applicable substantial web work, reuse the [shared scoped web contract](../../website-operating-rules/references/scoped-web-contract.md) when available. Preserve current authorization, stack and requested scope; this optional reference does not require another planning or approval cycle.

## Official Source Anchors

- React reference: https://react.dev/reference/react
- You Might Not Need an Effect: https://react.dev/learn/you-might-not-need-an-effect
- Next.js docs overview: https://nextjs.org/docs

## Submission integrity

Show success only after the adapter confirms its defined outcome; distinguish accepted/enqueued from delivered or completed. Preserve entered values on recoverable failure and provide an appropriate retry path. Pending UI prevents accidental repeats but does not replace backend duplicate protection for nonidempotent actions. Use the established backend idempotency/duplicate mechanism where applicable and test delayed responses, duplicate attempts and failures using an authorized test destination. Mockups must remain visibly mock/inactive and must not imply delivery.
