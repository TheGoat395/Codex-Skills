---
name: agent-evaluation-operations
description: "Evaluate agent and skill behavior or routing."
---

# Agent Evaluation Operations

Evaluate the claim the change is supposed to support, not the amount of new prompt text or the number of passing examples. Routine copyediting of a test comment, ordinary execution of one existing test, or a task that merely mentions agents does not require an evaluation program.

## Choose the evaluation mode

- **Agent workflow:** test the real prompt, model, tools, approvals, state, and failure paths.
- **Skill behavior:** test whether the skill triggers on the right requests, stays out of unrelated requests, cooperates with adjacent skills, and improves outcomes without excessive context or rigidity.
- **Release comparison:** hold the harness constant and compare the current baseline with the proposed change.

For evaluating a skill creation or behavior-bearing modification, read [skill behavior evaluation](references/skill-behavior-evaluation.md). Use [the regression corpus](references/regression-corpus.json) when testing synthetic public agent and Codex operating behavior. Validate the corpus with `python3 "${CODEX_HOME:-$HOME/.codex}/skills/agent-evaluation-operations/scripts/validate_regression_corpus.py"`.

## Specify before measuring

Record the evaluation claim, tested system, model/reasoning setting, prompt and skill versions, tool access, side-effect policy, attempt budget, acceptance threshold, and what would falsify the claim. Do not compare two runs that silently differ on these dimensions.

Build cases from real work: ordinary success, ambiguous input, missing data, conflicting evidence, missing access, unavailable tools, duplicate events, unsafe external actions, escalation, recovery, and every confirmed historical failure. Keep a small smoke set plus a growing regression set.

Trace run ID, tested-system version, model/reasoning setting, prompt and skill versions, tools, input class, structured result, error, latency, cost, and approval path. Redact or avoid sensitive payload capture by default.

Test retrieval and application separately. A skill may fail to trigger even when its rules are sound, or it may trigger and still fail to change behavior. Keep a small matched baseline and treatment set with identical prompts, inputs, model settings, tools, and viewports; score first attempts blind when subjective judgment matters.

## Score observable behavior

Prefer deterministic assertions for file state, structured fields, tool calls, authorization boundaries, and exact completion status. Use written rubrics for judgment. Calibrate model graders against examples and human review; do not let the candidate skill be the sole judge of its own success.

Measure:

- factual grounding and evidence quality;
- scope coverage and completion-state accuracy;
- tool and skill routing, including false-positive triggers;
- action correctness, policy/approval adherence, and reversibility;
- correction quality after contradictory evidence;
- latency, tokens/cost, retries, and human review;
- privacy, recoverability, and sensitive-data handling.

## Test collisions, not only positive triggers

Run positive, negative, adjacent, overlap, precedence, and co-invocation cases. Use `python3 "${CODEX_HOME:-$HOME/.codex}/skills/agent-evaluation-operations/scripts/analyze_skill_collisions.py" --root "${CODEX_HOME:-$HOME/.codex}/skills"` only to generate candidate pairs; lexical similarity is discovery evidence, not proof of a semantic collision.

Reject a skill change when it attracts unrelated work, duplicates an existing owner without a routing reason, weakens a capability floor, improves only the curated examples, or adds more context cost than demonstrated value.

## Gate releases

- Run baseline and treatment under the same harness.
- Require the proposed change to fix its target regressions without material degradation elsewhere.
- Fail the release when a required scenario, authorization boundary, cost budget, or quality threshold is missed.
- Test external calls in a sandbox, fixture, or dry-run path before production.
- Separate local structural validation, simulated behavior, and live production evidence.
- Preserve run identifiers, versions, aggregate scores, failures, and reviewer overrides while redacting sensitive payloads.

Do not infer safety, production readiness, or broad behavioral improvement from one successful demonstration.

## Correction loop

For recurring review feedback, preserve the original artifact, the correction, its source, the proposed destination, exceptions, and a holdout case. Treat collector, reviewer and maintainer as logical roles, using separate staffing only when authorized and justified. Gather raw evidence, verify and group it, then decide whether it becomes guidance, a component or token, a deterministic check, an exemplar, an evaluation fixture, a coverage gap, or no change. Rerun affected cases after accepted changes and watch whether the same complaint actually becomes less common.

The corpus validator checks structure only. Use the concrete synthetic dossiers and local observer example in [fixture execution](references/fixture-execution.md) to connect cases to real inputs and observed task state; an unexecuted case is not a model result.

Use Promptfoo or another project-local harness only when its telemetry, credentials, remote execution, and configuration have been reviewed. Route agent-system architecture to `$agent-orchestration-architecture`; route repository security to `$repository-release-security`.

## Optional specialists

For repository release checks, use repository-release-security only if installed; otherwise run the repository-required checks, inspect the patch for secrets and dependency changes, and preserve rollback. Its absence does not block an otherwise verified release.
