# Documentation And Evidence Conclusions

Read this reference when drawing conclusions from policies, contracts, specifications, manuals, source code, tests, benchmarks, account state, logs, or runtime observations.

## Classify the source statement

Determine whether the source provides:

- definition;
- mandatory requirement;
- prohibition;
- permission or capability;
- default behavior;
- recommendation;
- example;
- limit or threshold;
- marketing claim;
- observed result;
- proposed future behavior.

Do not turn `may` into `will`, a default into a requirement, an example into exhaustive behavior, or a recommendation into a governing rule.

## Establish applicability

Record:

- authority and whether the source controls the question;
- publication, effective, version, commit, or observation date;
- product, plan, jurisdiction, environment, branch, or account scope;
- prerequisites and feature flags;
- exceptions, precedence, and supersession;
- whether the text describes intended behavior or observed behavior.

If authority or sources conflict, use `evidence-reconciliation` before concluding.

## Match conclusion to verification layer

| Evidence | Warranted conclusion |
|---|---|
| Governing text | The rule requires, permits, or prohibits X within its scope |
| Product documentation | X is documented for the stated version and conditions |
| Source code | The inspected code implements path X, subject to build/runtime configuration |
| Configuration | X is structurally configured, not necessarily active |
| Passing build/static check | The checked artifact satisfies that check |
| Targeted runtime test | X occurred in the tested environment and case |
| Production observation | X was observed live at the recorded time and scope |
| Benchmark | Candidate A performed as measured under the benchmark protocol |

Do not infer live operation from documentation, universal behavior from one test, production readiness from a build, or general superiority from one benchmark.

## Resolve a documentary conclusion

Use:

```text
Question:
Controlling source and version:
Exact applicable rule or behavior:
Prerequisites/exceptions:
Observed implementation state:
Conflict or gap:
Strongest warranted conclusion:
Recheck trigger:
```

Quote only the minimum exact language needed. Preserve definitions and operative qualifiers.

## Verify independently

Ask verification questions without embedding the draft answer:

- Which source controls this situation?
- What version and scope apply?
- What must be true before the rule activates?
- What exceptions or precedence clauses exist?
- What observable evidence would show implementation?
- Does current state match the rule?

For a benchmark, independently check prompt, model/version, parameters, dependencies, hardware, repetitions, scoring, exclusions, uncertainty, and raw artifacts.

## Conclusion forms

- **Governing:** an applicable authority settles the rule.
- **Documented:** official text describes the capability or behavior.
- **Implemented:** source/configuration structurally contains it.
- **Observed:** direct evidence shows it occurred in a bounded case.
- **Verified in scope:** a suitable test establishes the stated behavior under recorded conditions.
- **Unsupported:** the source does not establish the proposed claim.
- **Applicability unresolved:** controlling scope, version, or prerequisite remains uncertain.

Keep these forms separate in the final wording.

## Research basis

- Dhuliawala et al., *Chain-of-Verification Reduces Hallucination in Large Language Models*: independent verification questions reduce anchoring to a draft in the evaluated tasks.
- Wu et al., *Large Language Models Can Self-Correct with Key Condition Verification*: reconstructing a decisive condition is more diagnostic than generic self-critique in the reported experiments.
- Local `evidence-reconciliation` and `deep-research` skills: authority, freshness, scope, directness, and contradiction govern source-backed conclusions.
