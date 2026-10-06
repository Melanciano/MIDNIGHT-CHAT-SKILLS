# Impeccable command playbooks — MIDNIGHT safe-core

These playbooks preserve the current upstream command surface while using only repository/local agent capabilities unless an Impeccable engine is separately verified.

## Build

### craft [feature]
Deprecated alias. Route to ordinary new-work: understand product truth and surface mode, shape the visual direction when needed, implement, then bounded verification.

### init
Inspect existing product/code context. Gather only material gaps. Write or update PRODUCT.md with users, product purpose, brand/voice, principles, factual constraints. If an implementation exists, offer DESIGN.md capturing visual truth. Never invent brand facts.

### document
Derive DESIGN.md from current code/assets: palette, typography, spacing, radii, elevation, motion, components, layout patterns, responsive rules, accessibility conventions, and visual atmosphere. Distinguish observed facts from inferred descriptions and ask for confirmation on subjective language.

### extract [target]
Find repeated UI patterns and drift. Consolidate reusable components/tokens with the smallest coherent change. Preserve behavior and public API unless scope says otherwise.

### shape [feature]
Do planning before code. Identify users/jobs, states, flows, information hierarchy, constraints, visual world, edge cases, accessibility, responsive behavior, and acceptance criteria. Produce a user-confirmed design brief before implementation.

## Evaluate

### critique [target]
Review UX: hierarchy, clarity, information architecture, cognitive load, affordances, emotional resonance, content, consistency, and task success. Separate evidence from taste. Score only dimensions that are actually observable and explain the scale.

### audit [target]
Inspect accessibility, contrast, keyboard/focus, semantics, responsive behavior, theming, motion/reduced-motion, loading/rendering, assets, overflow, error states, and obvious performance hazards. Report P0-P3 with evidence and an actionable plan. Do not claim automated detector output unless a detector actually ran.

## Refine

### polish [target]
Final bounded quality pass: alignment, spacing, rhythm, typography, consistency, interaction details, states, and visual defects. One inspect/fix pass plus at most one confirmation pass.

### bolder [target]
Increase visual impact while retaining usability and product truth. Strengthen composition, scale contrast, typography, color, art direction, motion, or imagery intentionally; avoid generic “AI gradient” decoration.

### quieter [target]
Reduce unnecessary intensity, competing accents, motion, contrast, density, decorative noise, and hierarchy conflicts while retaining identity.

### distill [target]
Remove nonessential elements, duplicated affordances, copy, visual containers, and decision burden. Preserve necessary function and accessibility.

### harden [target]
Make real-world states robust: empty/loading/error/offline, long/short text, i18n/RTL where relevant, overflow, destructive actions, permissions, unavailable data, malformed inputs, keyboard/touch, and recovery paths.

### onboard [target]
Design first-run/activation: value communication, progressive disclosure, setup, empty states, permission timing, contextual education, skip/resume, and measurable activation outcomes.

## Enhance

### animate [target]
Add motion only where it clarifies state, hierarchy, causality, spatial continuity, feedback, or delight. Respect reduced motion, performance, interruption, duration/easing consistency, and input modality.

### colorize [target]
Introduce purposeful color roles for hierarchy, action, state, grouping, brand, and emphasis. Verify contrast and dark/light theme interactions. Avoid using color as the only signal.

### typeset [target]
Improve font selection, scale, weight, line length, line height, hierarchy, numeric treatment, truncation/wrapping, variable-font use, and responsive typography. Preserve licensed/available font constraints.

### layout [target]
Fix composition, grid, spacing, rhythm, alignment, density, section hierarchy, whitespace, and responsive reflow. Test narrow/wide states and content expansion.

### delight [target]
Add memorable micro-details only after usability is sound: micro-interactions, transitions, empty-state personality, tactile feedback, surprising but comprehensible affordances. Do not obstruct task completion.

### overdrive [target]
Pursue technically ambitious presentation only when requested and suitable. Budget frame time, progressive enhancement, device capability, motion preferences, fallbacks, accessibility, and maintenance cost.

## Fix

### clarify [target]
Rewrite UX copy, labels, helper text, errors, confirmations, empty states, and instructions for actionability and plain language. Do not alter factual claims without evidence/approval.

### adapt [target]
Adapt across breakpoints/devices/platform contexts. Preserve task flow while adjusting information density, navigation, touch targets, layout, content prioritization, safe areas, input methods, and platform conventions.

### optimize [target]
Measure before claiming improvement. Inspect bundle/assets, render frequency, layout/paint work, animation, images, fonts, hydration, network waterfalls, list virtualization, and cache opportunities. Distinguish measured bottlenecks from hypotheses.

## Iterate

### live
True upstream live mode requires the verified Impeccable engine plus a running dev server/browser integration. Without it return `HOLD_IMPECCABLE_ENGINE_REQUIRED`. A user may explicitly accept a static alternative: generate normal code variants one at a time without calling it live/HMR.

### generate [n] [action] [element]
True agent-driven live variant cycling requires the verified engine. Without it, offer a static set of N clearly separated design proposals/patches only if the user accepts the downgrade; do not claim browser hot-swap.

## Ancillary upstream engine verbs

- `context`: load project/product/design/surface context.
- `pin <pin|unpin> <command>`: manage standalone command shortcut.
- `hooks <on|off|status|ignore-rule|ignore-file|ignore-value|reset>`: manage design detector hook.
- `doctor`: diagnose/repair Impeccable project-artifact drift.

In MIDNIGHT these ancillary verbs require a separately verified engine, except that context loading has the manual repository fallback described by the main skill.
