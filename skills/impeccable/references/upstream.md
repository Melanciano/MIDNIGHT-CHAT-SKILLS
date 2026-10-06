# Upstream provenance — Impeccable

Source repository: `pbakaus/impeccable`  
Pinned source ref: `ece38d9904b8a619b3f77cab476eacad09c4fb11`  
Upstream skill version: `4.5.0`  
Upstream engine version observed: `0.1.11`  
License: Apache-2.0. Third-party NOTICE retained alongside this port.

Public installation command:

~~~bash
npx skills add https://github.com/pbakaus/impeccable --skill impeccable
~~~

## Exact 24-command surface at the pinned ref

- `craft [feature description]`
- `init`
- `document`
- `extract [target]`
- `live`
- `generate [count] [direction] variants of [element]`
- `adapt [target] [context (mobile, tablet, print...)]`
- `animate [target]`
- `audit [area (feature, page, component...)]`
- `bolder [target]`
- `clarify [target]`
- `colorize [target]`
- `critique [area (feature, page, component...)]`
- `delight [target]`
- `distill [target]`
- `harden [target]`
- `onboard [target]`
- `layout [target]`
- `optimize [target]`
- `overdrive [target]`
- `polish [target]`
- `quieter [target]`
- `shape [feature to shape]`
- `typeset [target]`

Additional engine verbs described by upstream:
- `context`
- `pin <pin|unpin> <command>`
- `hooks <on|off|status|ignore-rule|ignore-file|ignore-value|reset>`
- `doctor`

Aliases:
- `teach` -> `init`
- `craft` -> deprecated ordinary new-work alias

## Upstream launcher audit

The upstream shell launcher searches for a supplied/local/cached engine and, as a last resort, can download the version-pinned release binary. A fresh download is checked against a `.sha256` sidecar and fails closed when verification is unavailable.

MIDNIGHT intentionally changes this:
- no automatic download;
- no chmod repair;
- no unverified PATH fallback;
- only `IMPECCABLE_BIN` or a sibling bundled binary that passes `engine-probe` may execute.

Therefore this is a functional safe-core port, not a byte-identical engine distribution.
