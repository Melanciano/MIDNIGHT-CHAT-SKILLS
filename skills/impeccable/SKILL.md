---
name: impeccable
description: Design, redesign, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend interface. Use for websites, landing pages, dashboards, product UI, components, forms, onboarding, responsive behavior, accessibility, performance, typography, layout, motion, UX copy, and design-system work. Not for backend-only tasks.
metadata:
  upstream: pbakaus/impeccable
  upstream_version: "4.5.0"
  midnight_port: safe-core-v1
---

# Impeccable — MIDNIGHT safe-core port

This is a source-pinned adaptation of `pbakaus/impeccable` under Apache-2.0. The 24 upstream command names and argument shapes are preserved. The binary engine is intentionally not vendored; see `references/upstream.md`.

## Core design laws

- The brief wins. Preserve explicit aesthetics, constraints, product truth, copy scope, and brand intent.
- Refinement preserves the incumbent identity; redesign may replace the visual world while retaining product truth and function.
- Inspect the existing implementation before editing. Missing DESIGN.md is not proof of greenfield.
- Distinguish surface mode:
  - Persuade: earn attention and action.
  - Operate: help the user complete a task.
  - Read: optimize comprehension.
  - Experience: let the artifact lead.
- Verify in bounded passes: build/inspect once, fix findings in one batch, confirm at most once more, then stop open-ended polishing.
- Respect accessibility, reduced motion, responsive behavior, contrast, content truth, localization, failure states, and performance.
- Do not introduce loaded extremist/militarist symbols as decorative motifs.

## Context setup

1. Inspect PRODUCT.md and DESIGN.md if present.
2. Inspect the target UI, styles, tokens, components, assets, visual regression fixtures, and screenshots when available.
3. If an already-verified Impeccable engine is supplied through `IMPECCABLE_BIN`, the safe launcher may run `scripts/impeccable context`.
4. If no engine is present, continue manually from repository context. Do not download an engine automatically.
5. Before UI edits, use `references/playbooks.md` and the relevant command entry below.

## Commands

| `craft [feature description]` | Deprecated compatibility alias for an ordinary Impeccable new-work request. It adds no behavior; natural build and redesign requests use the same flow. |
| `init` | Sets up a project for impeccable. Runs a multi-round discovery interview when context is missing and writes PRODUCT.md (strategic: users, brand, principles); offers DESIGN.md (visual: colors, typography, components) when code exists; pre-configures live mode; then recommends the best commands to run next. Every other command reads these files before doing work. Use once per project. |
| `document` | Generate a DESIGN.md file that captures the current visual design system. Auto-extracts colors, typography, spacing, radii, and component patterns from the codebase, then asks the user to confirm descriptive language for atmosphere and color character. Follows the Google Stitch DESIGN.md format so the file is tool-compatible. Use when you need a visual design spec an AI agent can follow to stay on-brand. |
| `extract [target]` | Pull reusable patterns, components, and design tokens into the design system. Identifies repeated patterns and consolidates them. Use when you have drift across the codebase and want to bring things back to a consistent system. |
| `live` | Interactive live variant mode. Select elements in the browser, pick a design action, and get AI-generated HTML+CSS variants hot-swapped via HMR. Requires a running dev server. Use when you want to visually experiment with design alternatives in real time. |
| `generate [count] [direction] variants of [element]` | Agent-driven live variant generation. Boots live mode, finds the named element on the open page, scrolls the browser to it, and delivers N variants in the requested direction for the user to cycle and accept. Use for requests that name an element and a direction, like 'generate 3 bold variants of the pricing cards', skipping manual element picking. |
| `adapt [target] [context (mobile, tablet, print...)]` | Adapt designs to work across different screen sizes, devices, contexts, or platforms. Implements breakpoints, fluid layouts, and touch targets. Use when the user mentions responsive design, mobile layouts, breakpoints, viewport adaptation, or cross-device compatibility. |
| `animate [target]` | Review a feature and enhance it with purposeful animations, micro-interactions, and motion effects that improve usability and delight. Use when the user mentions adding animation, transitions, micro-interactions, motion design, hover effects, or making the UI feel more alive. |
| `audit [area (feature, page, component...)]` | Run technical quality checks across accessibility, performance, theming, responsive design, and anti-patterns. Generates a scored report with P0-P3 severity ratings and actionable plan. Use when the user wants an accessibility check, performance audit, or technical quality review. |
| `bolder [target]` | Amplify safe or boring designs to make them more visually interesting and stimulating. Increases impact while maintaining usability. Use when the user says the design looks bland, generic, too safe, lacks personality, or wants more visual impact and character. |
| `clarify [target]` | Improve unclear UX copy, error messages, microcopy, labels, and instructions to make interfaces easier to understand. Use when the user mentions confusing text, unclear labels, bad error messages, hard-to-follow instructions, or wanting better UX writing. |
| `colorize [target]` | Add strategic color to features that are too monochromatic or lack visual interest, making interfaces more engaging and expressive. Use when the user mentions the design looking gray, dull, lacking warmth, needing more color, or wanting a more vibrant or expressive palette. |
| `critique [area (feature, page, component...)]` | Evaluate design from a UX perspective, assessing visual hierarchy, information architecture, emotional resonance, cognitive load, and overall quality with quantitative scoring, persona-based testing, automated anti-pattern detection, and actionable feedback. Use when the user asks to review, critique, evaluate, or give feedback on a design or component. |
| `delight [target]` | Add moments of joy, personality, and unexpected touches that make interfaces memorable and enjoyable to use. Elevates functional to delightful. Use when the user asks to add polish, personality, animations, micro-interactions, delight, or make an interface feel fun or memorable. |
| `distill [target]` | Strip designs to their essence by removing unnecessary complexity. Great design is simple, powerful, and clean. Use when the user asks to simplify, declutter, reduce noise, remove elements, or make a UI cleaner and more focused. |
| `harden [target]` | Make interfaces production-ready: error handling, i18n, text overflow, edge case management, and resilience under real-world data. Use when the user asks to harden, make production-ready, handle edge cases, add error states, or fix overflow and i18n issues. |
| `onboard [target]` | Design onboarding flows, first-run experiences, and empty states that guide new users to value. Covers welcome screens, account setup, progressive disclosure, contextual tooltips, feature announcements, and activation moments. Use when the user mentions onboarding, first-time users, empty states, activation, getting started, new user flows, or the aha moment. |
| `layout [target]` | Improve layout, spacing, and visual rhythm. Fixes monotonous grids, inconsistent spacing, and weak visual hierarchy. Use when the user mentions layout feeling off, spacing issues, visual hierarchy, crowded UI, alignment problems, or wanting better composition. |
| `optimize [target]` | Diagnoses and fixes UI performance across loading speed, rendering, animations, images, and bundle size. Use when the user mentions slow, laggy, janky, performance, bundle size, load time, or wants a faster, smoother experience. |
| `overdrive [target]` | Pushes interfaces past conventional limits with technically ambitious implementations — shaders, spring physics, scroll-driven reveals, 60fps animations. Use when the user wants to wow, impress, go all-out, or make something that feels extraordinary. |
| `polish [target]` | Performs a final quality pass fixing alignment, spacing, consistency, and micro-detail issues before shipping. Use when the user mentions polish, finishing touches, pre-launch review, something looks off, or wants to go from good to great. |
| `quieter [target]` | Tones down visually aggressive or overstimulating designs, reducing intensity while preserving quality. Use when the user mentions too bold, too loud, overwhelming, aggressive, garish, or wants a calmer, more refined aesthetic. |
| `shape [feature to shape]` | Plan UX and UI before code. Runs a required multi-round discovery interview, uses visual probes when available, and produces a user-confirmed design brief for implementation. |
| `typeset [target]` | Improves typography by fixing font choices, hierarchy, sizing, weight, and readability so text feels intentional. Use when the user mentions fonts, type, readability, text hierarchy, sizing looks off, or wants more polished, intentional typography. |

Routing:
- no command: present a context-aware menu; do not auto-run one;
- explicit or clearly implied command: follow its playbook in `references/playbooks.md`;
- `teach` aliases `init`;
- `craft` is a deprecated compatibility alias for ordinary new-work;
- if two commands genuinely fit, ask once which outcome the user wants.

## Engine-dependent capabilities

The upstream engine provides accelerated `context`, live-browser tooling, variant generation, pin/unpin shortcuts, detector hooks, and doctor/repair operations.

In this MIDNIGHT port:
- `live` and `generate` are `ENGINE_REQUIRED` for true hot-swap/HMR browser behavior;
- `hooks`, `doctor`, and `pin/unpin` are `ENGINE_REQUIRED`;
- `context` has a manual fallback and does not block ordinary design work;
- the launcher never downloads binaries.

If the user wants an engine-dependent function and no verified engine exists, return `HOLD_IMPECCABLE_ENGINE_REQUIRED` and offer the nearest static/manual workflow without pretending it is live mode.

## MIDNIGHT boundary

This skill does not grant deployment, publication, production, credential, browser-login, or authority permissions. UI edits remain subject to the current project grant and exact-head qualification. External visual claims must be evidence-backed; do not invent product facts or assets.
