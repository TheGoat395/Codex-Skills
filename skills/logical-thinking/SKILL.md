---
name: logical-thinking
description: Determine what follows from explicit premises, rules, evidence, documentation, or observations by selecting and executing the appropriate inference structure. Use when validity, entailment, contradiction, causality, probability, explanation, or the exact strength of a conclusion is central. Do not invoke merely to gather missing facts or broadly critique source quality.
---

# Logical Thinking

Produce the strongest conclusion the available premises warrant, including `unknown`, conditional, or no conclusion when appropriate. Logical rigor means choosing the right inference system, preserving meaning and scope, checking each decisive step, and refusing to strengthen the result beyond its proof obligations.

## Select, adapt, and implement the reasoning structure

Do not apply one universal chain-of-thought template.

1. **Select:** identify the reasoning modules the task requires.
2. **Adapt:** translate them into a compact task-specific structure.
3. **Implement:** fill that structure using the actual premises and verify decisive steps.

This task-routed approach is especially important for weaker or smaller models: the structure should constrain reasoning without adding irrelevant ceremony.

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

## Build the inference map

Use a compact structure for consequential problems:

```text
Target conclusion C:
Premises: P1, P2, ...
Hidden conditions: H1, ...
Inference family and rule:
Intermediate result I1:
Objection, exception, or rival R1:
Verification route:
Warranted conclusion and strength:
```

Distinguish linked premises, which work only together, from independent reasons. Mark where an intermediate result changes from established fact to probabilistic or defeasible support.

## Check each decisive step

For every inferential edge, ask:

- Does the operation or rule actually license this move?
- Are all required conditions present?
- Did scope, units, polarity, timeframe, or quantifier change?
- Could the premises be true while this result is false?
- Is an exception or alternative explanation still live?
- Is the step deductive, or has probability entered silently?
- Does the conclusion depend on information not present in the premises?

For universal claims, search for a counterexample. For necessity, construct a countermodel. For quantitative claims, use a calculator or executable check when available. For source-code or operational claims, prefer tests and observed behavior over prose inference.

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

## Verify with independent constraints

Generic self-critique is not verification. Prefer:

1. formal solver, parser, calculator, test, compiler, query, or runtime check;
2. authoritative source or direct record;
3. countermodel or boundary-case construction;
4. independent verification questions that do not embed the provisional answer;
5. key-condition reconstruction from the proposed conclusion;
6. a materially different solution path when the answer is externally checkable.

Use multiple paths selectively. Majority agreement is useful only when the paths are diverse and the target has a determinate answer; it is not evidence that a subjective preference is true.

## Choose the conclusion type before wording it

Use the narrowest form that answers the question:

- **No conclusion:** premises are irrelevant, materially ambiguous, or unusably inconsistent.
- **Unknown:** neither the conclusion nor its negation follows.
- **Conditional:** follows only if an exposed assumption holds.
- **Possible:** compatible with the evidence but not favored.
- **Best current explanation:** abductively stronger than tested rivals.
- **Probable within scope:** inductive or probabilistic support with conditions.
- **Strong empirical support:** converging direct observations within defined boundaries.
- **Defeasibly supported:** reasonable unless a named exception or critical question succeeds.
- **Deductively entailed:** follows necessarily from sound premises.
- **Causally identified:** supported at the stated association, intervention, or counterfactual level.
- **Governing/documented:** established by an applicable authority, not necessarily observed in operation.
- **Decision recommendation:** preferred action given objectives, uncertainty, costs, and reversibility.

Do not use `proven`, `must`, `causes`, `always`, or `impossible` unless the inference satisfies that burden.

## Run the adversarial pass

Before finalizing a material conclusion:

1. negate or vary the conclusion correctly;
2. construct the strongest case where the premises hold but the conclusion fails;
3. identify the weakest high-leverage premise;
4. test an alternate interpretation of the most ambiguous statement;
5. ask what additional premise would be required for a stronger result;
6. produce the narrowest conclusion that survives if the weakest premise is removed.

Revise only when the challenge supplies a valid reason. Do not abandon a correct result because an unsupported critique sounds cautious.

## Coordinate boundaries

Use `critical-thinking` when the central question is whether evidence, assumptions, incentives, or argument quality deserves confidence. Use `evidence-reconciliation` when conflicting authority or current source state controls. Use `deep-research` when premises must be discovered. Use `creativity` when the missing work is generating possibilities rather than adjudicating what follows.

## Deliver

For simple problems, apply the protocol silently and answer directly. For consequential problems, report the normalized premises, inference family, decisive rule or test, exceptions or unknowns, verification performed, and strongest warranted conclusion. Show enough structure to audit the result without dumping private scratch reasoning.
