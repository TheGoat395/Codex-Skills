---
name: logical-thinking
description: "Determine what premises and evidence warrant."
---

# Logical Thinking

Produce the strongest conclusion the available premises warrant, including `unknown`, conditional, or no conclusion when appropriate. Logical rigor means choosing the right inference system, preserving meaning and scope, checking each decisive step, and refusing to strengthen the result beyond its proof obligations.

## Scale the proof to the question

Adapt the inference family; do not impose a universal template. Preserve meaning, units, scope and quantifiers. Test whether premises can hold while the conclusion fails; use decisive calculations, solvers, tests or observations. Correlated self-review is not independent verification.

For **consequential, multi-step, ambiguous or contested inference**, read [proof and verification](references/proof-and-verification.md) plus the applicable family below for maps, step checks, conclusion types and adversarial tests. Simple entailment/calculation remains direct.

Use conditional or unknown when warranted. `Proven`, `must`, `causes`, `always` and `impossible` require their own proof burden.

## Normalize the problem

Before inference, identify:

- exact question and candidate conclusion;
- premises, observations, rules, and documentation;
- source/status of each premise: given, observed, documented, inferred, assumed, or disputed;
- definitions, entities, variables, units, timeframe, version, and domain;
- quantifiers and modal force: all, some, none, must, may, usually, likely;
- knowledge regime: closed world, open world, or incomplete real-world evidence;
- hidden premises required to connect the stated information.

Resolve semantic ambiguity before formalizing. Do not create precision by translating an unclear sentence into symbols without deciding what the sentence means.

## Choose the inference family

| Family | Appropriate question | Valid conclusion form |
|---|---|---|
| Deductive | Must the conclusion follow? | entailed, contradicted, or unknown |
| Defeasible/informal | Is the argument presumptively reasonable? | supported unless a critical exception succeeds |
| Inductive | How strongly do observations generalize? | scoped probability or empirical support |
| Abductive | Which explanation best accounts for the evidence? | best current explanation, not proof |
| Causal | What would happen under intervention or counterfactual change? | association, intervention effect, or counterfactual claim |
| Probabilistic | How should uncertainty update? | posterior or calibrated range under assumptions |
| Documentary/rule | What does an authority establish here? | governing, permitted, required, documented, or unresolved applicability |
| Decision | Which action is preferable under uncertainty? | recommendation conditional on goals and tradeoffs |

For formal entailment, natural-language arguments, exceptions, or scheme-based reasoning, read [formal and defeasible inference](references/formal-defeasible-inference.md).

For causal, probabilistic, forecasting, or decision reasoning, read [causal, probabilistic, and decision reasoning](references/causal-probabilistic-decision.md).

For conclusions from documentation, policies, tests, benchmarks, source code, or runtime evidence, read [documentation and evidence conclusions](references/documentation-evidence-conclusions.md).

## Keep unknown open

Under an open-world or incomplete-evidence regime:

- failure to prove C does not prove `not C`;
- failure to prove `not C` does not prove C;
- one absent fact does not license a closed-world assumption unless the system explicitly defines one;
- inconsistent premises do not justify an arbitrary conclusion in ordinary analysis.

Classify a deductive target as:

- **Entailed:** every model satisfying the premises satisfies C.
- **Contradicted:** every model satisfying the premises satisfies `not C`, or C directly conflicts with a controlling premise.
- **Unknown:** both C and `not C` remain compatible with the premises.
- **Premises inconsistent:** the premise set itself requires repair before ordinary inference.

This three-way classification is often more accurate than forcing true or false.

## Coordinate boundaries

Use `critical-thinking` when the central question is whether evidence, assumptions, incentives, or argument quality deserves confidence. Use `evidence-reconciliation` when conflicting authority or current source state controls. Use `deep-research` when premises must be discovered. Use `creativity` when the missing work is generating possibilities rather than adjudicating what follows.

## Deliver

For simple problems, apply the protocol silently and answer directly. For consequential problems, report the normalized premises, inference family, decisive rule or test, exceptions or unknowns, verification performed, and strongest warranted conclusion. Show enough structure to audit the result without dumping private scratch reasoning.
