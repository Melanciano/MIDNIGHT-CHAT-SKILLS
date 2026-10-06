---
name: skill-creator
description: Create, update, validate, evaluate, benchmark, package, and improve agent skills for MIDNIGHT/Codex. Use when a repeated workflow should become a reusable skill, when an existing skill needs refinement, or when skill triggering/output quality should be measured rather than guessed.
metadata:
  primary_upstream: anthropics/skills
  compatibility_upstream: openai/skills
  midnight_port: codex-eval-v1
---

# Skill Creator — MIDNIGHT / Codex adaptation

This skill combines two verified upstreams:

- Anthropic Skill Creator: rigorous draft → eval → baseline → grade → benchmark → review → iterate lifecycle.
- OpenAI/Codex Skill Creator: Codex-native structure, progressive disclosure, agents/openai.yaml, initialization and validation.

Read `references/upstream.md` before changing mechanics.

## Capture intent

Recover known workflow details from conversation, repository, corrections and examples before asking questions. Resolve what the skill enables, when it triggers/does not trigger, output artifacts, dependencies, authority boundaries, objective success criteria, and whether evals are meaningful.

Use `find-skills` first when an external skill may already solve the need.

## Structure and degrees of freedom

- High freedom: heuristics where multiple approaches are valid.
- Medium freedom: preferred workflow with bounded choices.
- Low freedom: deterministic scripts for fragile/repeated operations.

Keep SKILL.md concise. Move schemas/examples/variant detail to references and deterministic work to scripts.

## Initialize for Codex

From this skill directory:

~~~bash
python scripts/init_skill.py <skill-name> --path <target-parent> [--resources scripts,references,assets] [--examples] [--interface key=value]
python scripts/generate_openai_yaml.py <skill-dir> [--name <skill-name>] [--interface key=value]
python scripts/quick_validate.py <skill-directory>
~~~

Default MIDNIGHT target is the current repository's `.codex/skills/<skill-name>` unless another scope is explicitly intended.

## Evaluation lifecycle

1. Create 2–3 realistic task prompts initially. For trigger tuning, use a larger balanced set with hard positives and hard near-miss negatives.
2. For a new skill compare current candidate against no-skill baseline. For an existing skill snapshot the old skill and compare revised vs old.
3. Keep configurations isolated. Do not let one run's outputs become hidden context for the other.
4. Draft objective assertions where possible; use qualitative human review for subjective quality.
5. Grade each run with `text`, `passed`, `evidence`.
6. Aggregate deterministic benchmark data.
7. Review outputs plus benchmark with the human.
8. Improve the general mechanism, not only the examples, and repeat.
9. Expand tests after the initial loop stabilizes.

If independent agents/runs are unavailable, say so. A serial same-agent sanity check is lower independence and must not be represented as an independent benchmark.

The deterministic benchmark/viewer/package commands are installed by Stage 2 and documented in `references/upstream.md`.

## Description optimization

Anthropic's automated optimization uses `claude -p`; those upstream commands are preserved in the provenance reference but classified `UPSTREAM_CLAUDE_ONLY`.

For MIDNIGHT/Codex:
- create 8–10 diverse should-trigger prompts;
- create 8–10 difficult should-not-trigger near misses;
- test on the actual available skill/Codex surface when possible;
- revise on misses and false triggers;
- use held-out behavior to resist overfitting.

Never claim the Claude optimization loop ran unless it actually did on a separately authorized Claude CLI surface.

## MIDNIGHT qualification

For a repo skill:
1. focused validation/tests;
2. exact-head repository CI;
3. inspect actually executed steps;
4. update adoption registry/evidence;
5. then classify SHADOW_QUALIFIED.

A skill cannot grant authority, bypass HUMAN_RESERVED, access secrets, weaken security, or turn synthetic eval success into provider/runtime proof.
