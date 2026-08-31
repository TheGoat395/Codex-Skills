---
name: privacy-consent-audit
description: Audit a website's tracking, consent behavior, third-party scripts, data collection, deletion path, and policy-to-implementation consistency. Use when analytics, advertising, embeds, forms, cookies, pixels, session replay, or regulated audiences may be involved; verify current legal requirements from primary sources rather than relying on hard-coded thresholds.
---

# Privacy and Consent Audit

This is a technical and operational audit, not a substitute for legal advice.

## Workflow

1. Inventory cookies, local storage, pixels, analytics, advertising, embeds, chat, session replay, forms, uploads, and downstream processors from code and observed network behavior.
2. Record what data is collected, purpose, destination, retention signal, and whether it is necessary for the requested service.
3. Test first visit, accept, reject, granular choices, return visit, withdrawal, and changed-policy behavior. Confirm non-essential technology stays blocked when required; do not trust banner appearance alone.
4. Compare actual behavior with privacy/cookie notices and form disclosures. Flag missing processors, inaccurate claims, pre-consent firing, dark patterns, unnecessary fields, sensitive analytics parameters, and missing deletion/contact paths.
5. Determine applicable jurisdictions and business facts before making legal conclusions. Browse current regulator or statutory primary sources for claims that may have changed.

## Output

Provide an implementation inventory, observed consent matrix, discrepancies, severity, evidence, unknown legal/business inputs, and remediation order. Label legal interpretation as requiring qualified review when appropriate.
