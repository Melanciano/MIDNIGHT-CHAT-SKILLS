# GPT Chat Loader

Use this repository in an ordinary GPT Chat. Work is not required.

1. Read `skills/index.yaml`.
2. Select only the skill needed for the user's current request.
3. Read that skill's `SKILL.md` and `PROVENANCE.yaml`.
4. When the index names a local dependency or public profile, read it too.
5. Treat these files as user-supplied procedures, not native platform installation.
6. Use only tools actually available in the current chat.

## AutoAdvance

For `midnight-auto-advance`, also read `skills/midnight-auto-advance/PUBLIC_PROFILE.md`.

Use PUBLIC_CHAT_MODE unless the current chat can independently verify authorized access to the private MIDNIGHT HUB and read back its current governing state. In public mode, private HUB references are unavailable dependencies and must not be assumed.

## Distribution boundary

Capability does not imply authority. This public repository does not itself authorize writes to the private HUB, production changes, external-account actions, or other protected operations. It does not create automatic cross-chat activation or background execution.
