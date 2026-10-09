# Planning skills import provenance — 2026-10-09

Scope: repository-local SHADOW reference copies only. No runtime qualification or authority change.

- `prompt-master/SKILL.md` + `references/patterns.md` + `references/templates.md`: https://github.com/nidhinjs/prompt-master, observed main SHA `2bd92518e26bf659e21e3d9ab90573fcf3ddeccb`, MIT. Full upstream license: https://github.com/nidhinjs/prompt-master/blob/2bd92518e26bf659e21e3d9ab90573fcf3ddeccb/LICENSE
- `grill-with-docs/SKILL.md` + `domain-modeling/SKILL.md`: https://github.com/mattpocock/skills, observed main SHA `49dd158d1076134a641b33efb035946536778336`, MIT. License: https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/LICENSE
- `grilling/SKILL.md`: MIDNIGHT-CHAT-SKILLS `skills/grilling/SKILL.md`, first-party adaptation (qualified dependency with grill-me in stable release).

`grill-with-docs` is a thin orchestration skill. It requires both `grilling` and `domain-modeling` to be loaded explicitly. If the host cannot load these dependencies, fail visibly; do not claim native skill execution. Any glossary/ADR write requires scope authority.

Risk gates: inspect untrusted upstream instructions; no secret disclosure, uncontrolled shell commands, financial actions, GPU submissions, publication, deploy, or branch promotion. Review/qualify before enabling.

Rollback: delete `.codex/skills/{prompt-master,grilling,grill-with-docs,domain-modeling}` and the shadow index additions on this branch; leave preexisting skills untouched.
