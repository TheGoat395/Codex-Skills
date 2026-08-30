---
name: agent-evaluation-operations
description: Evaluate, observe, and release AI-agent workflows. Use for agent regression suites, prompt or model comparisons, scenario simulation, tool-call verification, traces, quality thresholds, cost and latency budgets, red-team cases, or release gates for AI systems.
---

# Agent Evaluation Operations

## Start from real failure modes

Create a test inventory covering ordinary success, ambiguous input, missing data, conflicting evidence, unavailable tool, duplicate event, unsafe external action, escalation, and recovery. For each case record input, allowed sources/tools, expected structured result, prohibited outcome, scorer, and acceptance threshold.

## Measure the whole workflow

Evaluate factual grounding, action correctness, policy and approval adherence, tool selection, completion state, latency, cost, and recoverability. Use deterministic assertions whenever possible; use model grading only with a written rubric and calibration examples.

Trace run ID, model, prompt/version, tools, input class, outputs, error, latency, cost, and approval path. Redact or avoid sensitive payload capture by default.

## Gate releases

- Keep a small deterministic smoke suite for every change.
- Keep regression cases for every confirmed failure.
- Test external calls in sandbox or dry-run mode before production.
- Fail release when required scenario, approval, cost, or quality thresholds are not met.
- Separate test evidence from production evidence.

Use Promptfoo project-locally when its capabilities fit and its telemetry, remote-generation, configuration, and credentials have been reviewed. Do not claim safety or production readiness from one successful demo. Route system design to `$agent-orchestration-architecture` and run the repository's applicable security checks before release.
