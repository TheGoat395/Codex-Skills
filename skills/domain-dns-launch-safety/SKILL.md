---
name: domain-dns-launch-safety
description: Plan and verify safe domain, DNS, hosting, HTTPS, canonical-host, and redirect changes for a website launch. Use for registrar or nameserver changes, Porkbun or other DNS providers, apex and www configuration, email-preserving migrations, SSL issues, and production cutovers where existing records and rollback matter.
---

# Domain and DNS Launch Safety

DNS changes are external production mutations. Inspect first; require explicit authorization before writes.

## Preflight

- Confirm domain, registrar, authoritative DNS host, hosting target, intended canonical hostname, and account owner.
- Capture the current record set and TTLs with timestamps. Identify MX, SPF, DKIM, DMARC, verification, subdomain, and other non-website records.
- Obtain provider-specific required records from current official documentation. Do not guess targets.
- Define rollback records and owner before the cutover.

## Change plan

Prefer the smallest record change. Do not replace nameservers when adding A/AAAA/CNAME/ALIAS records is sufficient. Protect business email and existing services. Avoid duplicate/conflicting records and unsupported apex CNAME configurations.

## Verification

Check authoritative answers and multiple resolvers as appropriate; apex and `www`; HTTP to HTTPS; canonical redirects; certificate coverage; mixed content; hosting-domain verification; critical subdomains; and email health when relevant. Account for TTL and negative caching without declaring propagation complete prematurely.

## Output

Produce current-state snapshot, exact proposed changes, preserved records, rollback, risk window, verification evidence, and unresolved ownership/access issues. Never expose registrar or DNS credentials.
