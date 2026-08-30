# Formal And Defeasible Inference

Read this reference when the task involves entailment, contradiction, natural-language argument reconstruction, quantifiers, conditionals, exceptions, or informal argument schemes.

## Preserve semantics before symbols

Translate one atomic proposition at a time. Record the domain and meaning of each predicate. Preserve:

- universal versus existential scope;
- negation scope;
- inclusive versus exclusive `or`;
- `if`, `only if`, `if and only if`, and `unless`;
- necessity, possibility, obligation, permission, and probability;
- time, identity, and reference resolution.

When two interpretations are plausible, branch explicitly. Do not select the interpretation that conveniently proves the desired conclusion.

## Core valid patterns

### Modus ponens

```text
If P, then Q.
P.
Therefore Q.
```

### Modus tollens

```text
If P, then Q.
Not Q.
Therefore not P.
```

### Hypothetical syllogism

```text
If P, then Q.
If Q, then R.
Therefore, if P, then R.
```

### Disjunctive syllogism

```text
P or Q.
Not P.
Therefore Q.
```

Confirm that `or` is inclusive or exclusive as intended and that all relevant alternatives are represented.

## Frequent invalid moves

- **Affirming the consequent:** P implies Q; Q; therefore P.
- **Denying the antecedent:** P implies Q; not P; therefore not Q.
- **Converse error:** treating `all A are B` as `all B are A`.
- **Quantifier reversal:** moving from `for every x, some y` to `there is one y for every x`.
- **Illicit existential import:** inferring that an A exists from a universal statement alone.
- **Scope shift:** changing population, timeframe, definition, or modal strength mid-argument.
- **Composition/division:** transferring a property from parts to whole or whole to parts without a rule.
- **Explosion from messy data:** treating ordinary inconsistent evidence as permission to infer anything.

## Necessary and sufficient conditions

For `P -> Q`:

- P is sufficient for Q.
- Q is necessary for P.
- The contrapositive `not Q -> not P` is equivalent.
- The converse `Q -> P` and inverse `not P -> not Q` are not equivalent without more information.

For a biconditional `P <-> Q`, both directions hold. Do not infer a biconditional from repeated co-occurrence.

## Quantifier checks

- To refute `all A are B`, one verified A that is not B is sufficient.
- To establish `some A is B`, one verified witness is sufficient.
- Failure to find a witness does not prove none exists unless search completeness is established.
- `Not all A are B` means at least one A is not B; it does not mean no A is B.
- `All A are not B` and `not all A are B` are different claims.

## Countermodel procedure

To test entailment:

1. assume every premise is true;
2. assume the target conclusion is false;
3. construct a coherent interpretation or case;
4. if one exists, the conclusion is not deductively entailed;
5. if none can exist under the rules, show the decisive derivation or use a solver when available.

To test contradiction, repeat with the negation of the target.

## Open-world classification

Given premises P and target C:

- `entailed` if P implies C;
- `contradicted` if P implies not C;
- `unknown` if P permits both C and not C;
- `inconsistent premises` if P has no coherent model under the chosen logic.

Do not replace `unknown` with a guess. FOLIO uses the analogous true/false/unknown task structure and shows that unknown cases are a distinct reasoning burden.

## Defeasible arguments

Many real arguments are presumptive, not deductive. Represent them as:

```text
Ordinarily, if conditions A hold, C is reasonable.
Conditions A appear to hold.
No defeating exception E is established.
Therefore C is defeasibly supported.
```

The conclusion must remain retractable if a relevant exception, stronger contrary reason, or failed critical question appears.

## Argument schemes and critical questions

### Expert opinion

- Is the expertise relevant to the exact claim?
- Is the opinion based on evidence or merely assertion?
- Is the source independent and accurately represented?
- Is there relevant expert disagreement?

### Analogy

- Are the shared properties relevant to the conclusion?
- Which material differences could block transfer?
- Does a stronger counteranalogy exist?

### Cause to effect

- Is the causal rule established at the needed level?
- Are prerequisites present and alternative paths controlled?
- Does the conclusion exceed association evidence?

### Practical reasoning

- Is the goal explicit and legitimate for the decision?
- Will the action plausibly advance it?
- Are alternatives, side effects, constraints, and reversibility covered?

## Process check

For a multi-step proof, record each intermediate claim, its parent premises, the rule used, and whether it is deductive or defeasible. Verify the first uncertain step before elaborating the rest.

## Research basis

- Han et al., *FOLIO: Natural Language Reasoning with First-Order Logic* (2022/2024): natural-language conclusions classified as true, false, or unknown with verified FOL annotations.
- Walton and Godden, *The Nature and Status of Critical Questions in Argumentation Schemes*: informal arguments are defeasible and evaluated with scheme-specific questions.
- Facione, *Critical Thinking: A Statement of Expert Consensus* (1990): interpretation, analysis, evaluation, and inference are distinct skills.
