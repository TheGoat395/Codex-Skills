# Skill behavior evaluation

## Evaluation contract

Define one falsifiable claim, such as: “This change reduces false completion claims on artifact-producing tasks without increasing unnecessary skill activation on simple questions.” Record the baseline skill set, treatment skill set, model/reasoning setting, available tools, context, attempt limit, and scoring rubric.

Do not use install count, instruction length, source reputation, or structural validation as behavioral proof.

## Case classes

| Class | Purpose | Passing evidence |
|---|---|---|
| Positive | A request clearly needs the skill | Correct activation and materially improved behavior |
| Negative | Similar vocabulary but different intent | Skill stays out or its rules do not distort the result |
| Adjacent | A neighboring skill should own the task | Correct routing without duplicated workflows |
| Overlap | Two skills plausibly apply | Stable precedence or useful co-invocation |
| Precedence | Instructions or sources conflict | Correct authority order and explicit reconciliation |
| Adversarial | The easy answer would overclaim | Evidence-based correction or bounded uncertainty |
| Economy | The skill adds context/process | Benefit justifies latency, tokens, and tool calls |

For every case, record the prompt, allowed resources, expected behavior, prohibited behavior, side effects permitted, scorer, threshold, and failure evidence. Protect credentials and private payloads; use synthetic or redacted fixtures where the content itself is not the capability being tested.

## Trigger-collision audit

1. Inventory names and frontmatter descriptions.
2. Generate lexical candidate pairs with `scripts/analyze_skill_collisions.py`.
3. Review candidates semantically. Similar descriptions can be intentional routing neighbors; different words can still hide the same workflow.
4. Decide one of: keep distinct, narrow one trigger, add explicit routing, merge into one owner, or make a specialist explicit-only when the user requests that policy.
5. Re-run positive and negative cases after any description change because discovery behavior changed even if the body did not.

## Baseline versus treatment

- Use identical prompts, tools, inputs, and budgets.
- Randomize or blind review order where practical.
- Preserve raw failure evidence and aggregate separately.
- Report regressions, not just mean score.
- Investigate disagreements between deterministic checks, model graders, and human judgment.
- Re-run a stable subset to detect variance before attributing a one-run improvement to the skill.

## Release decision

Release only when the target failures improve and no material capability floor regresses. Structural validation proves packaging only. Simulated scenarios prove harness behavior only. Neither proves performance on all future tasks or live production systems.

Primary anchors:

- OpenAI Evals: https://github.com/openai/evals
- OpenAI contextual evals: https://openai.com/index/evals-drive-next-chapter-of-ai/
- OpenAI evaluation validity guidance: https://openai.com/index/trustworthy-third-party-evaluations-foundations/
