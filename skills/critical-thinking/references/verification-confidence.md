# Verification And Confidence

Use this reference for consequential conclusions, uncertain model reasoning, factual synthesis, or any task where a confident but wrong answer would matter.

## Do not trust generic self-critique

An LLM examining its own answer without new structure or feedback can preserve the same error or replace a correct answer with a wrong one. Treat internal critique as hypothesis generation, not validation.

Do not ask only, "Is this correct?" Define a check that could fail independently.

## Select a verification route

Choose the strongest practical route:

1. **Executable check:** calculator, parser, theorem prover, compiler, test, query, schema validation, or runtime observation.
2. **Authoritative check:** governing document, primary record, official specification, or direct data.
3. **Independent questions:** derive fact-check questions from the draft, answer them separately, then compare.
4. **Key-condition reconstruction:** temporarily hide a decisive condition and test whether the proposed answer reconstructs it.
5. **Countermodel:** construct a case where the premises hold but the conclusion fails.
6. **Alternate path:** solve from a different representation, decomposition, or method and compare checkable outputs.

Use agreement among paths only when errors are plausibly independent. Restating the same reasoning in different words is not an independent check.

## Independent verification questions

After a provisional conclusion:

1. list the smallest factual or logical questions whose answers determine it;
2. phrase each question without embedding the provisional answer;
3. answer from the strongest accessible evidence or tool;
4. compare the independent answers with the draft;
5. revise only where the check supplies a reason.

For documentation, ask separately: What text controls? Which version? What scope? What prerequisites? What exceptions? Does live behavior match the documented rule?

For quantitative work, independently check units, denominator, reference period, formula, boundary conditions, and a rough-order estimate.

## Key-condition reconstruction

Use when one condition strongly determines the answer:

1. identify the decisive entity, value, rule, constraint, or premise;
2. remove it from the problem representation;
3. combine the remaining problem with the proposed conclusion;
4. infer what the missing condition would need to be;
5. compare that reconstruction with the actual condition.

A mismatch is evidence of an error. A match increases confidence but does not prove the entire chain.

## Process verification

For multi-step reasoning, inspect each step for:

- supported inputs;
- correct operation or inference rule;
- preserved scope and units;
- no dependency on a later conclusion;
- correct handling of unknowns;
- a checkable intermediate result.

An acceptable final result does not excuse an invalid intermediate step when the same flaw could fail elsewhere.

## Confidence dimensions

Calibrate confidence across four dimensions:

| Dimension | Low confidence when |
|---|---|
| Premises | sources are weak, stale, conflicted, or incomplete |
| Inference | a countermodel exists or the rule is defeasible and unanswered |
| Alternatives | credible rivals explain the evidence similarly well |
| Verification | checks are absent, correlated, or only intrinsic self-review |

Use the weakest decisive dimension to limit the overall conclusion. Do not average away a fatal gap.

## Stopping rule

Stop when decisive claims have checks proportionate to risk, the strongest countercase has been tested, no unresolved issue can materially change the conclusion, and additional checks are repetitive or lower-value.

## Research basis

- Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet* (2023): intrinsic self-correction can fail or degrade reasoning without external feedback.
- Dhuliawala et al., *Chain-of-Verification Reduces Hallucination in Large Language Models* (2023/2024): independently answering planned verification questions reduced hallucination in evaluated tasks.
- Wu et al., *Large Language Models Can Self-Correct with Key Condition Verification* (2024): targeted key-condition verification improved over generic self-correction in the studied tasks.
- Lightman et al., *Let's Verify Step by Step* (2023): process supervision outperformed outcome-only supervision in their mathematical-reasoning setting.
