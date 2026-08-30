---
name: deep-research
description: "Run adaptive, evidence-led, multi-pass research for consequential, complex, disputed, niche, or fast-changing questions without requiring repeated prompts for missing depth. Use for exhaustive research, due diligence, investigations, audits, fact checking, landscape mapping, comparative ranking, or source-backed decisions across any domain where coverage, freshness, contradictions, confidence, access recovery, and traceable claims matter."
---

# Deep Research

Produce a decision-ready result whose material claims can be traced to inspected evidence. Derive the necessary research universe from the objective, pursue it broadly and deeply in proportion to consequence, challenge the leading conclusion, and finish the natural in-scope work without waiting for follow-up prompts.

Read [references/evidence-standard.md](references/evidence-standard.md) completely before substantive research.

## Establish the Research Contract

1. Identify the decision, deliverable, or truth claim the research must support.
2. Derive scope, exclusions, time horizon, freshness, jurisdiction, acceptable uncertainty, and failure conditions from the request and governing sources.
3. Define observable acceptance criteria and what evidence could change the answer.
4. Read named governing files, records, datasets, accounts, repositories, or primary sources completely before claiming adoption.
5. Make reasonable reversible assumptions when they preserve the objective; surface only assumptions that materially affect the result.

Keep research read-only unless the request separately authorizes implementation, communication, purchasing, publication, or account mutation.

## Calibrate Depth

Classify the task before gathering evidence:

- **Focused:** resolve a bounded question with the smallest sufficient evidence.
- **Deep:** map the credible field, verify decisive claims, investigate contradictions, and recommend a direction.
- **Exhaustive:** derive the full relevant research graph, screen the broad field, deeply inspect the strongest bounded subset, run an adversarial completion pass, and create a decision-to-execution handoff in one invocation.

Treat explicit requests for deep, exhaustive, maximum, or complete research as exhaustive within the stated objective. Do not make the user discover and request natural subquestions one at a time. Do not make a focused task exhaustive merely because more sources exist.

## Derive the Coverage Graph

Before searching, infer the dimensions that could materially change the answer. Represent the task as a dynamic graph containing only applicable elements:

- questions, claims, unknowns, and decision criteria;
- relevant entities, artifacts, events, systems, and alternatives;
- relationships, dependencies, incentives, and conflicts;
- authoritative, independent, experiential, and contradictory evidence classes;
- time, version, geography, population, plan, environment, or other scope boundaries;
- available access surfaces and materially different fallback paths;
- practical constraints such as cost, capacity, complexity, ownership, risk, and scale;
- existing decisions or baselines that the result must confirm, revise, or reject.

Expand the graph when evidence reveals a material adjacent branch. Prune branches that cannot affect the decision. This graph, not a hardcoded source list or quota, determines coverage.

## Apply the Evidence Hierarchy

Use the strongest source appropriate to each claim:

1. Current explicit instructions and governing sources.
2. Verified live state and direct records.
3. Original authoritative evidence, including first-party data, official documentation, filings, standards, source code, and primary materials.
4. Independent analysis with visible methods and incentives.
5. Credible specialist reporting.
6. Community experience and anecdotal evidence as field signal.
7. Metadata, summaries, snippets, and remembered context only as discovery aids.

Verify unstable facts live. Test incentivized claims independently when the decision warrants it. Do not inflate confidence by counting multiple retellings of one origin as independent evidence.

## Run the Research Passes

### 1. Frame

Build the coverage graph, define comparison criteria, expose assumptions, and identify what would reverse the expected conclusion.

### 2. Discover

Map the credible field before selecting favorites. Search across materially different terminology, source origins, adjacent categories, counterexamples, and relationship paths implied by the graph.

### 3. Screen

Use lightweight evidence to rank relevance and evidentiary value. Deduplicate repeated origins, resolve uncertain identities, remove immaterial candidates, and choose a bounded high-value subset for deeper inspection. Size the funnel to the decision rather than a predetermined count.

### 4. Deepen

Inspect the complete evidence needed for each decisive claim. Preserve dates, scope, definitions, units, versions, exceptions, methods, and incentives. Follow citations and dependencies back to their strongest practical origin.

### 5. Challenge

Seek credible contrary evidence, negative cases, alternate explanations, incentive conflicts, methodological weaknesses, implementation failures, and omitted categories. Resolve conflicts by authority, currency, scope, method, and directness; leave genuine disputes visible.

### 6. Synthesize and Verify

Compare alternatives using one consistent framework. Separate verified fact, source-supported interpretation, inference, estimate, recommendation, disputed claim, and unknown. Verify that every material citation supports the exact nearby claim.

## Recover From Access and Search Failures

When material evidence cannot be reached through the preferred route:

1. classify what was actually accessible;
2. identify another authorized, documented, materially different access path;
3. retry using a different query, representation, interface, archive, export, index, or originating source when applicable;
4. record each meaningful attempt and result;
5. reduce the claim or confidence only after practical alternate routes are exhausted.

Never represent metadata, a title, a snippet, an inaccessible body, or another source's description as direct inspection.

## Maintain Resumable Research State

For long, multi-surface, or compaction-prone work, maintain a task-scoped checkpoint using the evidence standard. Keep it concise and recoverable. Record:

- objective, acceptance criteria, scope, and current thesis;
- coverage graph and status by material dimension;
- inspected sources and atomic claims;
- candidates screened versus deeply inspected;
- access failures and alternate attempts;
- contradictions, unresolved questions, and next highest-value actions;
- decisions changed during the challenger pass.

Resume from the checkpoint instead of restarting or relying on compressed conversation memory. Do not create durable files for a small task when an internal ledger is sufficient. Remove temporary artifacts after delivery unless they remain useful to the project or the user asks to retain them.

## Make Consecutive Passes Additive

When a research task is exceptionally ambiguous, high-impact, system-wide, or repeatedly unresolved, divide consecutive passes deliberately:

- **Pass 1 — Discovery and thesis:** map the field, build the evidence-backed working model, and identify decisive unknowns.
- **Pass 2 — Challenger and completion:** pursue omissions, counterevidence, weak identities, alternate interpretations, and unresolved branches; record what changed, survived, or remained uncertain.

Do not use the second pass to restate the first. De-escalate implementation or repetition once the difficult direction is settled.

## Run the Autonomous Completion Check

Before delivery, test whether a rigorous reviewer could expose a material omission by asking about:

- an adjacent entity, alternative, evidence class, relationship, or counterexample implied by the scope;
- a mismatch between claims and observable behavior, delivery, economics, incentives, or implementation;
- direct evidence versus inferred connection;
- current constraints, total cost, operational burden, ownership, scale, or failure behavior;
- duplication, regression, or an unjustified change from the existing baseline;
- an untried practical access route;
- evidence that points away from the initial belief or the working thesis.

Continue automatically when the omission is material and in scope. Do not expand into a different objective.

## Stop at Decision Sufficiency

Stop when:

- acceptance criteria are met;
- all material coverage dimensions are addressed or explicitly unresolved;
- decisive claims use the strongest practical evidence;
- contradictions, inaccessible evidence, and uncertainty are visible;
- the recommendation survives the challenger pass;
- additional work is unlikely to change the decision enough to justify its cost.

Do not stop at the first plausible answer. Do not continue collecting repetitive evidence after the decision is stable.

## Deliver the Result

Lead with the answer. Include only what the task needs:

1. decision or executive conclusion;
2. scope, date, method, and meaningful coverage;
3. decisive findings with exact citations;
4. comparisons or rankings when useful;
5. counterevidence, uncertainty, inaccessible evidence, and failed access paths;
6. recommendation, tradeoffs, and reconsideration triggers;
7. explicit status of what was verified, inferred, estimated, disputed, or not checked.

Never claim exhaustive coverage, direct access, source inspection, current state, or verification that the evidence ledger does not support.
