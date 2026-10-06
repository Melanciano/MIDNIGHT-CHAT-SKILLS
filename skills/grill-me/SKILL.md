---
name: grill-me
description: Explicit entry point for a relentless interview that sharpens a plan or design before action. Invoke only when the user asks to be grilled, stress-tested, challenged, or explicitly calls grill-me.
---

# Grill Me — MIDNIGHT wrapper

Upstream `mattpocock/skills` implements `grill-me` as a thin wrapper that delegates to `grilling`.

Do exactly that here:

1. Load the repo-scoped `grilling` skill.
2. Follow its interview protocol.
3. Do not execute the plan during the grilling session.
4. Finish only after the user confirms shared understanding.

If the runtime exposes explicit skill invocation, invoke `grilling`. Otherwise read `../grilling/SKILL.md` and follow it directly.

This wrapper is intentionally explicit-only. Do not silently start grilling ordinary requests.
