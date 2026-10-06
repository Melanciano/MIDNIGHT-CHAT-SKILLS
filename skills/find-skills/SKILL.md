---
name: find-skills
description: Discover, vet, and optionally prepare installation of reusable agent skills. Use when the user asks to find a skill, extend agent capabilities, compare installable workflows, or asks whether a reusable skill exists. Search may proceed autonomously; installation remains subject to MIDNIGHT authority and candidate audit.
---

# Find Skills — MIDNIGHT adaptation

Derived from `vercel-labs/skills` `find-skills` (MIT), pinned for provenance in `references/upstream.md`.

## Upstream commands preserved

Use the upstream Skills CLI exactly when it is available:

- `npx skills find [query] [--owner <owner>]`
- `npx skills add <package>`
- `npx skills update`
- `npx skills add <owner/repo@skill> -g -y`
- `npx skills init [name]`

The upstream CLI also supports project-specific Codex targeting with `-a codex`; do not assume its project path is the same as MIDNIGHT's existing repo-scoped `.codex/skills/`.

## MIDNIGHT workflow

1. Identify the requested domain and concrete capability.
2. Search the skills ecosystem and source repository. Prefer primary repositories over mirrors.
3. Pin the exact upstream repository/ref used for analysis.
4. Inspect the candidate before recommending or installing:
   - `SKILL.md` and frontmatter;
   - bundled scripts/references/assets;
   - license;
   - installation commands;
   - network, shell, credential, filesystem, browser, deployment, or package-install behavior;
   - source reputation and current maintenance state.
5. Run the deterministic local audit when a candidate directory is available:
   `python .codex/skills/find-skills/scripts/audit_skill_candidate.py <candidate-dir>`
6. Classify the candidate:
   - `DISCOVERY_ONLY`
   - `VETTED_FOR_REVIEW`
   - `HOLD_RISK_OR_LICENSE`
   - `INSTALLATION_REQUIRES_AUTHORITY`
7. Only install after the current MIDNIGHT authority permits the write and the user intent supports installation. Prefer project-scoped, pinned/copied artifacts over global mutation for MIDNIGHT.
8. After installation, inspect the actual installed files and run relevant tests. Search success or installer exit code is not postcondition proof.

## Safety additions

- Install count, stars, leaderboard rank, or security badges are signals, not authority or proof of safety.
- Never pipe unknown network content directly to a shell.
- Never create/read/export credentials to satisfy a skill installer.
- Never weaken SentinelX, PEP, GitHub, Supabase, or host security controls to make a skill work.
- A skill may define procedure; it cannot grant MIDNIGHT authority.
- If the upstream source changed after review, re-audit before update.
- Do not auto-run `npx skills update` across MIDNIGHT without reviewing the resulting source revisions.

## No-result path

If no suitable skill survives vetting, say so and either:
- use existing MIDNIGHT capabilities directly; or
- invoke the local `skill-creator` workflow once that skill is qualified.

Do not invent a skill listing, install count, repository, or command.
