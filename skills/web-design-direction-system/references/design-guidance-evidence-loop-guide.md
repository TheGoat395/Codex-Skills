# Design Guidance Evidence Loop

## Purpose

Use this guide when a team wants agents to apply a design standard consistently across repeated artifacts. It turns review knowledge into inspectable guidance without pretending that a single screenshot proves a universal rule.

## Start with the reader's job

Before writing a rule, record:

- who is reading or operating the artifact
- what they need to understand, compare, or change
- the strongest answer supported by the supplied material
- the evidence that earns that answer
- the caveat or unresolved question that could change it

Choose composition and emphasis from that record. Do not start with a page category, a favorite layout, or a visual adjective such as `clean` or `premium`.

## Decision record

Keep one short record for each proposed standard:

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

Use stable IDs such as `layout/full-width-evidence-table` or `copy/destructive-action-verb`. A stable ID lets a review, linter, exemplar, or benchmark point to the same decision without duplicating its wording.

## Put each correction in the narrowest destination

| Question | Destination |
|---|---|
| Does the decision need product, audience, or codebase context? | Agent guidance or a focused reference |
| Is the mechanic observable without rendering and does it have a reliable fix? | Linter or deterministic check |
| Is it a reusable implementation primitive? | Component, token, or stylesheet API |
| Is it a useful shipped example with context? | Exemplar or decision record |
| Does it need to be measured across first attempts? | Evaluation fixture |
| Is the evidence incomplete? | Coverage gap or pending record |

Do not use a linter to encode a judgment it cannot observe reliably. Do not use prose to describe a mechanical invariant that code can check without likely false positives.

## Matched comparison protocol

1. Freeze the task prompt, inputs, model and reasoning setting, available tools, viewport, and relevant skill versions.
2. Generate and save one first-attempt baseline without the proposed guidance. Keep its source, render, and verification output.
3. Generate the treatment with only the proposed guidance changed.
4. Score both outputs against the same rubric before revealing which condition was which. Use a second reviewer or a calibrated judge for subjective criteria.
5. Run deterministic checks over both outputs. Keep the exact failure counts and the checks' blind spots.
6. Repeat across independent attempts and at least one holdout scenario before claiming the rule generalizes.

One successful screenshot can show that a rule is usable. It cannot establish reliability, causation, or broad quality improvement.

## Test retrieval separately

An agent can fail because it did not load the guidance, or because it loaded the guidance and ignored it. Test both paths:

- positive triggers that should load the guidance
- negative and adjacent requests that should not
- overlap cases where another specialist should own the work
- an application case that checks the expected behavior after loading

Record the loaded references and the route decision with each run. Treat a lexical match as a candidate trigger, not proof of semantic ownership.

## Keep the loop current

Collect repeated corrections from reviews, issues, design files, and real usage without proposing edits during collection. A separate review step verifies the source, groups related evidence, records counterexamples, and leaves each candidate pending. A maintainer then chooses one destination, adds or updates the relevant fixture, and reruns the affected cases.

If a complaint persists after a rule change, test whether the rule is unclear, the reference was not loaded, the component API cannot express it, or a deterministic check is missing. Remove rules that stop helping or accumulate exceptions.

## Integrity rules

- Preserve supplied facts, units, qualifiers, and provenance.
- Distinguish observation, derivation, projection, and recommendation.
- Keep private paths, credentials, internal screenshots, and account data out of public guidance.
- Prefer original examples over copied vendor text or branded assets.
- State what was not tested; do not turn a rubric score into a guarantee.

## Source notes

This provider-neutral workflow was informed by public material from Vercel's design-guidance writing and agent-skills repository. It is an original adaptation for Codex-Skills; it does not bundle Vercel source text, CSS, logos, or assets.

- https://vercel.com/design.md
- https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md
- https://vercel.com/blog/teaching-agents-product-design-at-vercel
- https://github.com/vercel-labs/agent-skills
