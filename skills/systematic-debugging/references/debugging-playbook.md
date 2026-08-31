# Debugging playbook

## Minimal incident record

| Field | Record |
|---|---|
| Expected | Observable intended result |
| Observed | Exact failure, not interpretation |
| Scope | Users, routes, machines, data, versions, or environments affected |
| First/last known state | Time or revision anchors |
| Reproduction | Command or interaction and frequency |
| Baseline | Whether it failed before current changes |
| Consequence | Data, money, trust, availability, quality, or developer time |
| Evidence | Logs, traces, screenshots, response bodies, tests, diffs |

## Layer probes

| Layer | High-value probes | Common false conclusion |
|---|---|---|
| Test | Run focused and isolated; compare order and shared state | “The test is flaky” without identifying why |
| Build/type | Read first causal error; verify toolchain and generated inputs | Fixing downstream errors before the first failure |
| Browser/UI | Console, network, DOM, computed styles, viewport, state | Source looks correct, therefore rendered behavior is correct |
| API/integration | Request contract, auth, timeout, retry, destination receipt | HTTP acceptance equals business delivery |
| Database/data | Query, schema, constraints, transaction, representative data | UI deduplication fixes a data-model defect |
| Dependency | Lockfile, resolved version, release notes, current official docs | Remembered API behavior is still current |
| Environment | Runtime versions, variables by name, permissions, filesystem, locale | “Works on my machine” disproves the defect |
| State/race | Timing, concurrency, order, leaked globals, cache, retry | A successful retry proves the system is reliable |
| Performance | Profile first; long tasks, waterfall, asset, allocation, query | Micro-optimization fixes an unmeasured bottleneck |

Never print secret values while comparing environments. Compare presence, source, checksum, or redacted shape where possible.

## Hypothesis ledger

Limit the active set to materially different explanations. For each:

1. State a falsifiable hypothesis.
2. Name evidence that supports and contradicts it.
3. Choose the cheapest safe test whose result differs between hypotheses.
4. Run it once and record the actual result.
5. Retire, refine, or confirm the hypothesis.

Do not turn temporal sequence into causality without a discriminating test. Do not “shotgun” dependency upgrades, cache clearing, reinstalls, and code edits together; a recovered system with no known cause is hard to trust and easy to regress.

## Intermittent failures

- Increase observability around the suspected seam while redacting sensitive data.
- Compare isolated versus suite/order-dependent execution.
- Vary concurrency, latency, clock, locale, and representative state one dimension at a time.
- Preserve the first failing trace and the first succeeding trace under matched conditions.
- When reproduction remains unavailable, report the leading hypotheses and next signal instead of inventing a cause.

## Escalation

Escalate from local repair to architectural review when the same defect survives materially different serious attempts, the required invariant has no stable seam, or a fix would create cross-system inconsistency. Record attempts and evidence before changing direction.

Primary inspiration: https://github.com/addyosmani/agent-skills/blob/main/skills/debugging-and-error-recovery/SKILL.md
