# Upstream provenance — grill-me / grilling

Source: `mattpocock/skills`  
Pinned upstream main observed during adoption: `24fe0ef7737efae15c87225755e9f6f5965e4888`  
License: MIT, copyright Matt Pocock 2026.

## Current upstream structure

`skills/productivity/grill-me/SKILL.md` is an explicit-only wrapper. Its operational body delegates to the skill named `grilling`.

`skills/productivity/grilling/SKILL.md` contains the actual interview engine:
- decision tree;
- frontier;
- rounds;
- numbered questions;
- recommended answer for each question;
- environment fact gathering instead of asking the user;
- completion only when the frontier is empty and shared understanding is confirmed.

## Public install command

The catalog publishes:

~~~bash
npx skills add https://github.com/mattpocock/skills --skill grill-me
~~~

For a self-contained copy, include both dependencies:

~~~bash
npx skills add mattpocock/skills --skill grill-me --skill grilling
~~~

MIDNIGHT vendors an adapted repo-scoped pair instead of running the installer.

## Version note

Some documentation/mirrors describe older behavior as “ask one question at a time.” The pinned current upstream `grilling/SKILL.md` instead asks the whole independent frontier in each round. MIDNIGHT follows the pinned source file, not stale summaries.

## MIDNIGHT modifications

- Claude-specific “Skill tool” delegation is translated into Codex-compatible repo-skill loading.
- explicit-only invocation remains preserved for `grill-me`;
- MIDNIGHT authority/HUMAN_RESERVED boundaries are added;
- the final output includes explicit deferred/unknown/evidence fields;
- no automatic execution after the interview.
