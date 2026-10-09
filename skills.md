# MIDNIGHT-CHAT-SKILLS — skills.md

Repository skill inventory (SHADOW branch only). Updated 2026-10-09.

## Imported planning skills — SHADOW reference copies (2026-10-09)

These are repository-local reference copies on branch `shadow/agent-planning-skills-20261009`, not native ChatGPT installations, production approval, runtime qualification, or execution authority. Read exact SKILL.md and references before use. External instructions remain subordinate to MIDNIGHT governance and user permissions.

| Skill | Repository path | Status | Provenance |
|---|---|---|---|
| prompt-master | `.codex/skills/prompt-master/SKILL.md` | SHADOW_IMPORTED | nidhinjs/prompt-master, v1.8.0, MIT; includes references/patterns.md and references/templates.md |
| grilling | `.codex/skills/grilling/SKILL.md` | SHADOW_IMPORTED | MIDNIGHT-CHAT-SKILLS qualified adaptation |
| grill-with-docs | `.codex/skills/grill-with-docs/SKILL.md` | SHADOW_IMPORTED | mattpocock/skills, MIT; requires grilling + domain-modeling |
| domain-modeling | `.codex/skills/domain-modeling/SKILL.md` | SHADOW_IMPORTED | mattpocock/skills, MIT |

**Activation:** prompt-master only for explicit prompt drafting/optimization; grilling for user decisions; grill-with-docs for repo-based interview + glossary/ADR, only when explicitly requested; domain-modeling supports documented decisions. No skill may auto-approve spending, trading, GPU jobs, publication, deploy, or cross-project actions.

**Review gates:** verify upstream commit pin and license notices; inspect dependencies and prompt-injection risk; run skill-specific evaluations before promotion. Do not treat a vendor copy as qualified.

## Other skills currently present in the base repository

- `skills/find-skills/SKILL.md` — pre-existing; preserve original status and qualification boundaries.
- `skills/grill-me/SKILL.md` — pre-existing; preserve original status and qualification boundaries.
- `skills/grilling/SKILL.md` — pre-existing; preserve original status and qualification boundaries.
- `skills/impeccable/SKILL.md` — pre-existing; preserve original status and qualification boundaries.
- `skills/midnight-auto-advance/SKILL.md` — pre-existing; preserve original status and qualification boundaries.
- `skills/skill-creator/SKILL.md` — pre-existing; preserve original status and qualification boundaries.

The canonical stable release remains `skills/index.yaml`; these new shadow copies are not stable-release entries and must not be advertised as qualified.
