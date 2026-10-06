# Upstream provenance — find-skills

Source: `vercel-labs/skills`  
Pinned upstream main observed during adoption: `18f96ea131dab3b0fcc9b27cf7c6f6cbb6174680`  
Upstream path: `skills/find-skills/SKILL.md`  
License: MIT, copyright Vercel, Inc. 2026.

## Commands present in the upstream skill

```bash
npx skills find [query] [--owner <owner>]
npx skills add <package>
npx skills update
npx skills add <owner/repo@skill> -g -y
npx skills init my-xyz-skill
```

The current upstream CLI README additionally documents:

```bash
npx skills use <source>
npx skills list
npx skills remove [skills]
npx skills init [name]
npx skills add <source> --skill <skill> -a codex --copy
```

These additional CLI commands are reference capabilities of the Skills CLI, not claims that the original `find-skills` SKILL.md invokes all of them.

## MIDNIGHT modifications

MIDNIGHT adds:
- pinned provenance;
- deterministic local candidate audit;
- authority and security gates before installation/update;
- no global install by default;
- exact installed-file readback requirement.

The upstream text is not treated as authority.
