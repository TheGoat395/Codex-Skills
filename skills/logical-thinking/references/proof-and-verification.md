# Proof And Verification

Loaded only for the mode declared in [SKILL.md](../SKILL.md). Apply the relevant sections; preserve the requested objective and scope.

## Select, adapt, and implement the reasoning structure

Do not apply one universal chain-of-thought template.

1. **Select:** identify the reasoning modules the task requires.
2. **Adapt:** translate them into a compact task-specific structure.
3. **Implement:** fill that structure using the actual premises and verify decisive steps.

This task-routed approach is especially important for weaker or smaller models: the structure should constrain reasoning without adding irrelevant ceremony.

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
- **Deductively entailed:** follows necessarily from the stated premises. Soundness additionally requires valid reasoning and true premises.
- **Associational:** an observed relationship without an identified causal effect.
- **Causally identified:** an intervention or counterfactual claim supported by an explicit identification argument and its assumptions.
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
