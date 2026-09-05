# Design Guidance Evidence Loop

## Purpose

Use this guide when repeated work needs a design standard to produce consistent, inspectable decisions. It turns review evidence into guidance without treating one screenshot or preference as a universal rule.

## Start with the reader's job

Before writing a rule, record:

- who will use or read the artifact;
- what they need to understand, compare, decide, or change;
- the strongest answer supported by the available material;
- the evidence that earns that answer;
- the caveat or unresolved question that could change it.

Choose composition and emphasis from that record. Do not start with a page category, favorite layout, or vague adjective such as `clean` or `premium`.

## Decision record

Use a compact record for each proposed standard:

```text
# Decision: <short name>
Status: proposed | accepted | rejected
Scope: <surfaces, components, or artifact types>
Decision: <observable behavior>
Rationale: <reader or product consequence>
Evidence: <links, files, runs, or review records>
Exceptions: <when this does not apply>
Bad example: <observable failure>
Good example: <observable correction>
Assumptions: <facts still being checked>
Open decisions: <questions needing an owner>
```

Use a stable ID such as `layout/full-width-evidence-table`. This lets reviews, checks, exemplars, and evaluations point to the same decision without duplicating its wording.

## Choose the narrowest destination

| Question | Destination |
|---|---|
| Does the decision require product, audience, or codebase context? | Focused guidance or reference |
| Is the mechanic reliably observable without rendering? | Deterministic check |
| Is it a reusable implementation primitive? | Component, token, or stylesheet API |
| Is it a useful shipped example with context? | Exemplar or decision record |
| Must it be measured across first attempts? | Evaluation fixture |
| Is the evidence incomplete? | Pending record or coverage gap |

Do not use a linter for judgment it cannot observe reliably. Do not leave a mechanical invariant in prose when code can check it with low false-positive risk.

## Matched comparison

1. Freeze the prompt, inputs, model and reasoning setting, tools, viewport, and relevant skill versions.
2. Save one first-attempt baseline without the proposed guidance, including source, render, and verification output.
3. Generate a treatment with only the proposed guidance changed.
4. Score both against the same written rubric before revealing which is which when subjective judgment matters.
5. Run deterministic checks over both and preserve their failure counts and blind spots.
6. Repeat across independent attempts and at least one holdout scenario before claiming the rule generalizes.

One successful screenshot proves only that a rule can work in that case. It does not establish reliability, causation, or broad quality improvement.

## Test retrieval separately

An agent can fail because it did not load the guidance or because it loaded the guidance and ignored it. Test both:

- positive requests that should load it;
- negative and adjacent requests that should not;
- overlap cases where another specialist owns the work;
- application cases that verify behavior after loading.

Record loaded references and the routing decision with each run. A lexical match is a candidate trigger, not proof of semantic ownership.

## Keep the loop current

Collect repeated corrections from reviews, issues, design files, and real usage without editing standards during collection. A separate review verifies sources, groups related evidence, records counterexamples, and leaves candidates pending. A maintainer then selects the destination, updates the relevant fixture, and reruns affected cases.

If a complaint persists after a rule change, test whether the rule is unclear, was not loaded, cannot be expressed by the component API, or lacks a deterministic check. Remove rules that stop helping or accumulate too many exceptions.

## Integrity rules

- Preserve supplied facts, units, qualifiers, and provenance.
- Distinguish observation, derivation, projection, and recommendation.
- Keep private paths, credentials, internal screenshots, and account data out of public guidance.
- Prefer original examples over copied vendor text or branded assets.
- State what was not tested; do not turn a rubric score into a guarantee.

## Source notes

This provider-neutral workflow was informed by Vercel's public design-guidance and agent-skills material, then adapted for these private Codex skills.

- https://vercel.com/design.md
- https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md
- https://vercel.com/blog/teaching-agents-product-design-at-vercel
- https://github.com/vercel-labs/agent-skills
