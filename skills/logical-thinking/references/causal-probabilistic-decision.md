# Causal, Probabilistic, And Decision Reasoning

Read this reference when the task involves causality, uncertainty, forecasting, risk, or choosing an action.

## Separate three causal levels

Do not answer a stronger causal question with weaker evidence:

1. **Association:** What tends to occur with X? `P(Y | X)`
2. **Intervention:** What happens if X is deliberately changed? `P(Y | do(X))`
3. **Counterfactual:** What would have happened to this case under a different X?

Observational association alone does not generally identify intervention or counterfactual effects. State the highest level the evidence supports.

## Build a causal map

Identify:

- treatment or proposed cause;
- outcome;
- common causes/confounders;
- mediators on the causal path;
- colliders caused by two variables;
- selection mechanisms and missingness;
- feedback, time order, and reverse causality;
- intervention actually represented by the evidence.

Do not control automatically for every available variable. Conditioning on a mediator changes the estimand; conditioning on a collider can create spurious association.

## Evaluate causal identification

Ask:

- Is the cause prior to the outcome?
- Is there a plausible mechanism?
- What confounders or selection effects remain?
- Is exposure assigned, randomized, naturally varied, or self-selected?
- Are comparison groups exchangeable enough for the claim?
- Could measurement, attrition, or post-treatment conditioning create the result?
- Does the result transport to the target population and intervention?
- What sensitivity analysis or negative control could challenge it?

Use causal language only when an identification strategy, not merely a narrative, supports it.

## Probabilistic updates

For uncertain claims:

1. define the event and reference class;
2. identify the prior or base rate;
3. assess how likely the evidence is under each live hypothesis;
4. check dependence among evidence sources;
5. update direction and magnitude;
6. report a calibrated range when exact probability is unsupported.

Avoid:

- base-rate neglect;
- denominator omission;
- treating dependent signals as independent confirmations;
- confusing `P(evidence | hypothesis)` with `P(hypothesis | evidence)`;
- interpreting a confidence interval as the probability that a fixed parameter lies inside it;
- giving precise percentages without data or calibration.

When numbers matter, calculate explicitly and check units and boundary cases.

## Inductive generalization

Evaluate sample frame, selection, size, measurement reliability, heterogeneity, missingness, and applicability. A large biased sample can be less informative than a smaller representative one.

State:

- population observed;
- population claimed;
- conditions under which transfer is expected;
- uncertainty from sampling versus uncertainty from model or measurement assumptions.

## Abductive explanation

Compare hypotheses using:

- coverage of important observations;
- prior plausibility;
- mechanism and coherence;
- simplicity without ignoring anomalies;
- novel predictions;
- fit with negative evidence;
- evidence that discriminates rather than merely agrees.

The best current explanation is defeasible. Do not call it proven merely because alternatives are less developed.

## Forecasting

Use a relevant reference class before an inside-view story. Separate:

- base rate;
- case-specific adjustments;
- leading indicators;
- scenario dependencies;
- forecast horizon;
- resolution criterion.

Provide ranges or scenarios when uncertainty is material. Name what observation would cause an update.

## Decision reasoning

Truth and action are different outputs. A decision can be rational without the most likely scenario being certain.

Map:

| Element | Treatment |
|---|---|
| Objective | What result or value controls? |
| Options | Include status quo, staged, reversible, and information-gathering options |
| Outcomes | Benefits, harms, distribution, and second-order effects |
| Uncertainty | Scenario probabilities or qualitative confidence |
| Cost | Money, time, attention, opportunity, support, and switching |
| Downside | Tail risk, lock-in, irreversibility, and failure recovery |
| Information value | Could a cheap test change the choice? |
| Constraints | Authority, capacity, prerequisites, and deadlines |

Choose the action that best fits the user's objective and risk posture. Do not smuggle your own values into a supposedly logical conclusion.

## Research basis

- Shpitser and Pearl, *Complete Identification Methods for the Causal Hierarchy* (2008): association, intervention, and counterfactual levels require different information.
- Ibeling and Icard, *Probabilistic Reasoning Across the Causal Hierarchy* (2020): formalizes the increasing expressive power of association, intervention, and counterfactual languages.
- Wang et al., *Self-Consistency Improves Chain of Thought Reasoning* (2022): diverse reasoning paths can improve determinate reasoning tasks, but agreement should not be mistaken for independent evidence.
