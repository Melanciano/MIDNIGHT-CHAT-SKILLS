---
name: midnight-auto-advance
description: Continue an authorized MIDNIGHT mission across successive verified frontiers without expanding authority. Use when the user says AutoAdvance, auto advance, continue autonomously, prossiga em auto advance, or asks MIDNIGHT to keep progressing until a real blocker. Orchestrates existing MIDNIGHT Auto-Advance governance/runtime contracts; it does not replace or weaken them.
metadata:
  midnight_origin: first-party
  lifecycle: QUALIFICATION_ACTIVE
  authority_effect: NONE
  production_effect: NONE
---

# MIDNIGHT AutoAdvance

AutoAdvance is a reusable orchestration layer for mission continuity. It turns a governing human instruction into repeated bounded progress while preserving current MIDNIGHT authority, security, evidence, and runtime boundaries.

It is **continuation, not implicit authority**.

## Trigger

Use when the user explicitly selects AutoAdvance or clearly asks MIDNIGHT to continue the current authorized mission autonomously.

Examples:
- "Prossiga em AutoAdvance."
- "Use AutoAdvance até encontrar um bloqueio real."
- "Continue sozinho dentro do escopo já autorizado."
- "Retome esta missão em AutoAdvance."

Do not trigger merely because the user is silent, because a tool exists, or because a previous mission once used AutoAdvance. If AutoAdvance is already active for the current mission, a follow-up such as "prossiga" continues that mission; outside an active AutoAdvance mission, "prossiga" alone does not activate this skill.

## Governing contracts

Before material action, resolve the current versions of:
- `governance/auto-advance-v3.md`
- `governance/implicit-auto-advance-v1.md`
- `governance/roadmap-auto-advance-v4-adaptive-evidence-grounded.yaml`
- `runtime/auto_advance_v2_shadow.py`
- `runtime/implicit_auto_advance_v1_shadow.py`
- current durable state, frontier, authority/grant and exact Git/artifact binding.

Use `midnight-preflight` when state may be stale. This skill never duplicates those contracts as a competing authority source.

## Mission-persistent activation

Once explicitly selected for a mission, AutoAdvance remains active for subordinate implementation steps until:
- the mission completes;
- the user says STOP/PAUSE or materially changes the objective;
- a continuity breaker or mandatory stop state is reached;
- current authority/state/evidence cannot be refreshed;
- the available platform prevents further authorized execution.

Do not ask for approval of technical micro-decisions already covered by the Mission Continuity Envelope. Prefer conservative INTERNAL_REVERSIBLE_DEFAULT or safer OPERATIONAL_EQUIVALENT choices when permitted.

## Core cycle

Repeat while at least one frontier remains eligible:

1. **REFRESH** — resolve current repository/artifact head, durable state, authority/grant, frontier and required capabilities. Chat/memory alone is not current-state proof.
2. **DEFINE** — bind objective, success, verification, falsification and stop conditions.
3. **ROUTE** — use the current Cognitive Router / execution class and available tools.
4. **GROUND** — maintain epistemic status and provenance-bound evidence for material claims.
5. **FILTER** — enforce authority, prerequisites, tool availability, budget, security, reversibility and frontier eligibility.
6. **SELECT** — choose one eligible material frontier using the current evidence-grounded selection contract.
7. **ACT ONE BOUNDED FRONTIER** — execute only through tools actually exposed and authorized in the current surface.
8. **OBSERVE + VERIFY** — obtain readback/postcondition evidence. Tool success is not automatic effect proof.
9. **RECONCILE** — if effect is DISPATCHED/UNKNOWN or response is lost, reconcile before retry; use `frontier-reconcile` when applicable.
10. **CHECKPOINT** — persist verified progress/evidence when an authorized write surface exists.
11. **NEXT FRONTIER** — park blocked frontiers, inspect independent eligible frontiers, and continue automatically.

One material frontier per cycle does not mean one frontier per user turn. Multiple verified cycles may run in one invocation.

## Capability-gap recovery

A CAPABILITY/ENVIRONMENT/PROVIDER blocker should not immediately become a human question.

Try, in order, only when each candidate remains within the mission envelope:

`REUSE_NATIVE -> REUSE_CONNECTED -> COMPOSE_EXISTING -> CONNECT_AVAILABLE -> WRAP_PROVIDER -> BUILD_ADAPTER -> BUILD_MIDNIGHT_NATIVE -> HUMAN_DECISION/BLOCKED`

Never weaken a gate to route around it.

### Compose with find-skills

When the blocker is missing capability and discovery is useful, invoke the loaded `find-skills` protocol automatically:
- prefer primary/upstream sources;
- review license, scripts, network/shell/file/credential behavior and dependencies;
- distinguish chat-usable procedure from unavailable runtime features;
- do not auto-install merely because a candidate exists.

### Compose with skill-creator

If no suitable external capability exists, AutoAdvance may invoke `skill-creator` automatically to draft or implement a first-party MIDNIGHT skill only in the same authorized SHADOW/development scope.

Skill creation does not authorize native installation, production activation, credentials/secrets access, spend, publication, merge/promotion, or security weakening.

After creating a skill, validate it using the actual available surface before treating it as operational.

## Chat and scheduler adapters

### GPT Chat adapter
In ordinary GPT Chat, apply this procedure using only currently exposed tools. Repository persistence can make the protocol reloadable by a later conversation, but does not create a native automatic trigger.

If the chat surface ends or loses tools, persist a durable handoff/checkpoint when possible. A future conversation must refresh current state before resuming.

### Scheduled adapter
If an actual scheduling surface is available and the user has requested recurring execution, use the existing scheduled adapter/governance. Each scheduled run must refresh canonical state before action and remains bound by the same mission envelope.

Do not claim background or scheduled execution unless a scheduler was actually created.

## Mandatory holds / continuity breakers

Preserve the governing list in `implicit-auto-advance-v1.md`. In particular, stop or park the affected frontier for:
- new objective or scope expansion;
- authority expansion or stale/unknown authority;
- stale/unknown durable state;
- new credential/secret surface;
- new external counterparty or representation effect;
- new personal/regulated data class or cross-project raw payload movement;
- non-zero spend outside the ceiling;
- destructive/irreversible effect outside the envelope;
- legal/contractual commitment, capital movement or job application;
- public exposure, production promotion/protected merge, governance/gate change;
- required independent review;
- unresolved HUMAN_PREFERENCE / PERSONAL_FACT / AUTHORITY_FACT.

A blocker on frontier X does not stop independent eligible frontier Y.

## Output and attention

Prefer useful progress over narration. During long runs, keep updates compact and report only verified milestones, blockers and materially changed assumptions. Do not ask low-value questions that can be resolved from current sources/tools.

On terminal stop, report verified work completed, parked/blocked frontiers and blocker classes, unresolved UNKNOWNs, last durable checkpoint/evidence when available, and the next user action if one is actually required.

Use one explicit terminal state when applicable:
- `COMPLETE`
- `WAIT_EXTERNAL`
- `HOLD_HUMAN`
- `HOLD_EVIDENCE`
- `HOLD_CAPABILITY`
- `RECONCILE_REQUIRED`
- `HOLD_REVIEW`

## Qualification and self-correction

The active qualification contract is `governance/midnight-auto-advance-qualification-v1.yaml`.

During qualification:
- treat one material frontier as one cycle: select -> act -> readback -> postcondition -> reconcile -> checkpoint;
- permit self-correction only as a versioned SHADOW change with the material diff, reason and test result preserved;
- do not change a case mid-run and count the modified case as the same PASS;
- after three cycles without new evidence, try a new safe evidence/capability path within existing authority, then use `HOLD_REVIEW` if still blocked;
- compare against the defined baseline using observable decisions, stops, refresh, reconcile and continuity rather than textual sophistication;
- require an independent fresh-chat review without providing the executor's PASS/FAIL conclusion;
- P0/P1 reviewer findings keep the qualification in `HOLD_REVIEW` until corrected and re-reviewed;
- do not classify the skill `SHADOW_QUALIFIED` until every promotion requirement in the qualification contract is evidenced.

Track the qualification metrics defined in that contract; requested/intended counts are never evidence of measured completion.

## Nonclaims

This skill does not:
- grant new authority;
- activate production/runtime autonomy by itself;
- prove a provider effect without readback;
- make GPT Chat run after the conversation ends;
- make repository persistence equivalent to native skill installation;
- turn synthetic/eval success into live-provider proof.
