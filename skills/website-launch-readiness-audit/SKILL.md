---
name: website-launch-readiness-audit
description: Run a read-only, evidence-based website launch audit spanning functionality, responsive behavior, accessibility, performance, SEO, security, privacy, analytics, infrastructure, content, and operational readiness. Use before production launch or after major changes; do not implement fixes unless the user separately authorizes changes.
---

# Website Launch Readiness Audit

Audit first. Do not modify code, accounts, DNS, or production state unless the user explicitly asks for fixes.

## Establish scope

Identify the stack, environments, important routes, primary conversions, authentication/payment/data flows, intended markets, third parties, and available test evidence. Mark inaccessible surfaces as untested rather than passing them.

## Inspect

1. Build/test status and unresolved placeholders.
2. Rendered phone, tablet, and desktop behavior; navigation, links, forms, media, loading, success, error, empty, and destructive states.
3. Keyboard access, focus, semantics, labels, contrast, alt text, reduced motion, and captions where applicable.
4. Core Web Vitals risks, asset weight, fonts, third parties, hydration, layout shift, and animation cost.
5. Titles, descriptions, canonical URLs, crawl controls, sitemap, headings, structured data, and local-business consistency.
6. Secrets, authentication, authorization, database rules, payment gates, webhooks, rate limits, headers, logging, and dependency risk—only where applicable.
7. Tracking inventory, consent behavior, policy-to-implementation consistency, data minimization, and third-party disclosure.
8. DNS/HTTPS/redirects, monitoring appropriate to risk, backups for stateful systems, rollback, ownership, and handoff.

Use narrower installed audit skills for specialist checks. Verify current legal, platform, or standards claims from primary sources when they affect a finding.

## Rating

- **BLOCKER:** credible launch-stopping security, payment, privacy, data-loss, or primary-conversion failure.
- **HIGH:** users cannot reliably complete an important task or a major audience is excluded.
- **MEDIUM:** material quality, discoverability, performance, or operational weakness.
- **LOW:** bounded polish or resilience improvement.

Never fail a site merely because it lacks dark mode, analytics, a PWA manifest, Terms of Service, or a named vendor. Judge applicability and risk.

## Output

Give an executive ship/no-ship recommendation, evidence table, blockers, prioritized findings with affected paths/routes, untested areas, and a smallest-safe remediation sequence. Distinguish observed facts from inferences.
