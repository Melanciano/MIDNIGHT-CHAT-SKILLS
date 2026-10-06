---
name: grilling
description: Stress-test a plan, decision, or idea through a structured decision-tree interview. Use when grill-me delegates here or the user explicitly asks for a rigorous interrogation of their thinking.
---

# Grilling — MIDNIGHT adaptation

Interview the user until you reach shared understanding. Model the subject as a **decision tree**: each decision may unlock dependent decisions.

## Rounds and frontier

Work in rounds. The **frontier** is every unresolved decision whose prerequisites are already settled.

For each round:
1. Recompute the frontier.
2. Ask every independent frontier question that can be answered now.
3. Number the questions.
4. Give your recommended answer for each question.
5. Wait for the user's answers before advancing to dependent questions.

Do not ask a question in the current round when its answer depends on another unresolved question in the same round.

Use this shape:

~~~text
❓ Q1 — <question title>: <question>

➡️ <recommended answer>

---

❓ Q2 — <question title>: <question>

➡️ <recommended answer>
~~~

## Facts vs decisions

Finding facts is the agent's job. Before asking the user for a factual detail that can be established from:
- the current conversation;
- repository/files;
- connected tools;
- current provider readback;
- trustworthy external sources;

look it up instead.

If fact gathering is still in progress, treat it as an unresolved prerequisite only for downstream questions that depend on it; continue with other independent frontier questions.

Decisions belong to the user. Recommendations do not become decisions merely because the agent prefers them.

## MIDNIGHT boundary

- This is an interview/reasoning skill, not an execution grant.
- It cannot expand authority, convert HUMAN_RESERVED work into autonomous work, or treat a user-facing recommendation as PEP permission.
- Do not write code, deploy, mutate infrastructure, install packages, send messages, or otherwise act on the plan during the grilling session unless the user explicitly ends the interview and starts a separately authorized execution task.
- If a decision depends on stale or unknown live state, identify the missing evidence rather than guessing.
- Preserve UNKNOWN, DEFERRED, and explicit trade-offs in the final summary.

## Completion

The session is complete when:
- the frontier is empty;
- every material branch is decided, resolved, explicitly deferred, or marked unknown with required evidence;
- no material assumption remains silent; and
- the user confirms shared understanding.

Then return a concise decision map containing:
- decisions;
- rationale;
- deferred items;
- unresolved evidence;
- risks/trade-offs;
- next authorized frontier.

Do not start executing the resulting plan automatically.
