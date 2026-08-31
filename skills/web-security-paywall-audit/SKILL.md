---
name: web-security-paywall-audit
description: Audit web security for secrets, authentication, authorization, paid-content enforcement, payment replay, database access controls, webhooks, API abuse, rate limits, sensitive logs, headers, and production exposure. Use for websites or apps with accounts, payments, AI endpoints, private data, uploads, or server APIs; remain read-only unless fixes are requested.
---

# Web Security and Paywall Audit

Treat repository evidence as partial. Do not claim a control works without tracing the relevant client, server, database, and provider boundary.

## Threat paths

1. Inventory public/client code, server routes, data stores, privileged keys, payments, webhooks, uploads, AI calls, and administrative actions.
2. Trace who can call each sensitive operation and where identity and authorization are enforced.
3. For paid content, verify the server stores or derives the protected result and releases it only after server-side entitlement verification. CSS hiding, client state, obfuscation, and teaser/full payloads sent together are failures.
4. Verify payment references cannot be replayed across users or purchases and webhook signatures use the provider's official verification method.
5. Inspect database/RLS or equivalent policies, tenant isolation, service-role placement, storage rules, and deletion/update authorization.
6. Check secret exposure, unsafe public environment prefixes, source maps/logs, verbose errors, CORS/origin assumptions, rate limiting, resource exhaustion, and upload constraints.
7. Check browser security headers in context. Do not prescribe a header that breaks the application without a tested policy.

Use current official provider documentation for payment, database, authentication, and webhook requirements.

## Evidence standard

For every finding include attack path, affected asset, evidence, realistic impact, confidence, and the control that should exist. Separate confirmed vulnerabilities from defense-in-depth recommendations.

## Output

Prioritize exploitable secret/data/payment/authorization failures first. Include unreviewed surfaces and safe verification steps. Never print live secrets or sensitive user data.
