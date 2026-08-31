---
name: analytics-conversion-verification
description: Define, inspect, and verify website conversion measurement for calls, forms, directions, bookings, orders, reservations, purchases, and other qualified actions. Use for analytics implementation or QA, event naming, ownership, consent-aware loading, production debugging, and reporting that must connect traffic to business outcomes.
---

# Analytics and Conversion Verification

Measure business outcomes, not event volume.

## Workflow

1. Confirm business goal, primary and secondary conversions, production domain, analytics owner, approved provider, consent requirements, and reporting audience.
2. Create an event map with action, trigger, parameters, destination, deduplication, success definition, and test method. Avoid personal or sensitive data in parameters.
3. Inspect implementation and observed production behavior. Verify events fire once, only after the real action threshold, with correct domain/environment and consent state.
4. Test phone, directions, forms, bookings, orders, reservations, and purchases end to end where in scope. A click is not a completed conversion unless the business intentionally defines it that way.
5. Confirm internal/test traffic handling, cross-domain flows, attribution limitations, ownership, and documentation.

Do not add a tracker merely to satisfy a checklist. Do not enable non-essential tracking before applicable consent and approval controls.

## Output

Return the measurement plan, observed-versus-expected matrix, duplicate/missing events, privacy risks, untested provider steps, and reporting recommendations.
