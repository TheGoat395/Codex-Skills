---
name: agent-orchestration-architecture
description: "Resolve agent ownership and handoff design."
---

# Agent Orchestration Architecture

## Design in escalating complexity

Choose the lightest design that satisfies the outcome:

1. Deterministic program or promptless automation.
2. One agent with bounded tools and structured output.
3. One manager agent that calls specialists as bounded tools.
4. Handoffs only when a specialist should own the rest of the interaction.
5. Durable workflow runtime only when work survives interruptions, waits, or external callbacks.

Do not use an agent swarm as a substitute for an owned workflow.

## Define the operating contract

Before implementation, record:

- outcome, success evidence, and named final-output owner;
- inputs, output schema, permitted tools, and forbidden actions;
- model and reasoning choice by decision difficulty, not task size;
- state owner, memory lifetime, tenant boundary, and source of truth;
- approval checkpoints, budgets, timeouts, stop conditions, and escalation;
- retry, idempotency, compensation, and human-handoff behavior.

Parallelize only independent work whose outputs can be reconciled without conflicting writes.

## Make control explicit

- Use a manager when one agent must enforce shared policy, combine specialist work, or own the user-facing answer.
- Use a handoff when the specialist needs a focused interaction and clear transfer of responsibility.
- Pass structured task packets, not vague conversation history. Minimize context to the specialist's need.
- Delegate only a concrete, independent workstream with a defined output. Parallelism can reduce latency, but every subagent performs separate model and tool work and therefore increases usage.
- Designing a delegation architecture does not authorize spawning agents. Follow current global and native tool constraints: preserve the selected parent model/effort and apply the current global child-model and reasoning policy. Do not freeze a session-specific model or effort into this specialist. Use only supported context controls and sufficient task context; do not override native inheritance constraints for a preferred packet format.
- Give each specialist the exact sources, constraints, output schema, stopping condition, and useful result-size limit. Ask for distilled findings instead of raw logs or copied source material.
- Keep the parent thread as the canonical decision owner. Do not spawn several agents to reread the same corpus, and do not use subagents merely to avoid doing a bounded task locally.
- Use inherited authorization for routine reversible in-scope writes, drafts and configuration. Require explicit authorization for actual sends, spending, binding commitments, publication and materially irreversible actions at their real boundaries; do not reopen an already clear authorization.
- Design every loop with a maximum attempt count and a useful terminal state.

## Required outputs

For a material architecture request, produce the smallest useful combination of an execution diagram, role/tool matrix, state/approval map, operating limits, and evaluation plan. Do not create every artifact for a simple routing decision. Route persistent-context design to `$agent-memory-provenance`; route quality and release testing to `$agent-evaluation-operations`; route external events to `$integration-contract-reliability`.

## Optional specialists

For external events, integration-contract-reliability is optional. Without it, define typed inputs/outputs, authentication, idempotency, retries, duplicate handling, uncertain-effect reconciliation and the actual success boundary in the project contract.
