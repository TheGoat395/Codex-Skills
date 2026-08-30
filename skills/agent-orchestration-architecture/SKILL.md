---
name: agent-orchestration-architecture
description: Design reliable AI-agent and multi-agent systems. Use when deciding whether a workflow needs one agent, tools, specialist agents, manager control, handoffs, durable execution, human approval, model routing, retries, or an operating boundary for an AI workflow.
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
- Keep external writes, money, sending, publishing, and irreversible operations behind explicit approval gates.
- Design every loop with a maximum attempt count and a useful terminal state.

## Required outputs

Produce an execution diagram, role/tool matrix, state and approval map, operating limits, and an evaluation plan. Route persistent-context design to `$agent-memory-provenance`; route quality and release testing to `$agent-evaluation-operations`; define explicit integration contracts for external events.
