#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

RISK_PATTERNS = {
    "pipe_to_shell": re.compile(r"(curl|wget)[^\n|]*\|\s*(sh|bash|zsh)\b", re.I),
    "destructive_rm": re.compile(r"\brm\s+-[^\n]*r[^\n]*f\b|\brm\s+-rf\b", re.I),
    "sudo": re.compile(r"\bsudo\b", re.I),
    "credential_terms": re.compile(
        r"(private[_ -]?key|api[_ -]?key|access[_ -]?token|refresh[_ -]?token|client[_ -]?secret)",
        re.I,
    ),
    "shell_exec": re.compile(r"\b(os\.system|subprocess\.|child_process|execSync|spawnSync)\b"),
    "network_exec": re.compile(r"\b(curl|wget|requests\.|fetch\(|urllib\.|axios\.)\b", re.I),
    "chmod_chown": re.compile(r"\b(chmod|chown)\b", re.I),
}

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".sh", ".bash", ".zsh", ".js", ".ts", ".tsx", ".jsx",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".ps1", ".cmd",
}
MAX_FILE_BYTES = 1_000_000


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    out: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: audit_skill_candidate.py <candidate-dir>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(json.dumps({"ok": False, "error": "CANDIDATE_DIR_NOT_FOUND"}))
        return 2

    skill_md = root / "SKILL.md"
    files = []
    findings = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = str(path.relative_to(root))
        size = path.stat().st_size
        row = {"path": rel, "bytes": size, "sha256": sha256(path)}
        files.append(row)
        if size > MAX_FILE_BYTES:
            findings.append({"path": rel, "kind": "large_file", "detail": str(size)})
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"SKILL.md", "LICENSE"}:
            text = path.read_text(encoding="utf-8", errors="replace")
            for kind, pattern in RISK_PATTERNS.items():
                if pattern.search(text):
                    findings.append({"path": rel, "kind": kind})

    frontmatter = parse_frontmatter(skill_md) if skill_md.exists() else {}
    if not skill_md.exists():
        findings.append({"path": "SKILL.md", "kind": "missing_skill_md"})
    if not frontmatter.get("name"):
        findings.append({"path": "SKILL.md", "kind": "missing_name"})
    if not frontmatter.get("description"):
        findings.append({"path": "SKILL.md", "kind": "missing_description"})

    license_files = [
        row["path"] for row in files
        if Path(row["path"]).name.lower().startswith(("license", "copying", "notice"))
    ]

    result = {
        "ok": skill_md.exists() and bool(frontmatter.get("name")) and bool(frontmatter.get("description")),
        "root": str(root),
        "name": frontmatter.get("name"),
        "description_present": bool(frontmatter.get("description")),
        "file_count": len(files),
        "license_files": license_files,
        "findings": findings,
        "files": files,
        "classification": (
            "HOLD_REVIEW_FINDINGS" if findings
            else "VETTED_STRUCTURE_NO_STATIC_RISK_SIGNAL"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
