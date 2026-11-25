#!/usr/bin/env python3
"""Validate the EIDOS Agent Skill structure, frontmatter, links, context budget, and WCAG token math."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = ROOT / "SKILL.md"
TOKENS_JSON = ROOT / "templates" / "design-tokens.json"

MAX_NAME_LEN = 64
MAX_DESC_LEN = 1024
MAX_SKILL_LINES = 220
MAX_REF_LINES = 220


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md is missing valid YAML frontmatter delimited by ---")
    raw_fm, body = match.group(1), match.group(2)
    data: dict[str, str] = {}
    current_key: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        if current_key is not None:
            data[current_key] = " ".join(x.strip() for x in buffer if x.strip())

    for line in raw_fm.splitlines():
        if re.match(r"^[a-zA-Z0-9_-]+:\s*", line):
            flush()
            key, val = line.split(":", 1)
            current_key = key.strip()
            val = val.strip()
            buffer = [] if val in (">-", ">", "|", "|-", "") else [val]
        elif current_key is not None and (line.startswith("  ") or line.startswith("\t")):
            buffer.append(line.strip())
    flush()
    return data, body


def validate_frontmatter(errors: list[str], warnings: list[str]) -> None:
    if not SKILL_MD.exists():
        errors.append("Missing required SKILL.md at skill root")
        return
    text = SKILL_MD.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > MAX_SKILL_LINES:
        warnings.append(
            f"SKILL.md has {len(lines)} lines (recommended <= {MAX_SKILL_LINES} for progressive disclosure)"
        )

    try:
        fm, _ = parse_frontmatter(text)
    except ValueError as exc:
        errors.append(str(exc))
        return

    name = fm.get("name", "")
    desc = fm.get("description", "")

    if not name:
        errors.append("Frontmatter missing required field: name")
    else:
        if len(name) > MAX_NAME_LEN:
            errors.append(f"Frontmatter name exceeds {MAX_NAME_LEN} chars: {len(name)}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"Frontmatter name must be lowercase hyphenated alphanumeric: {name!r}")
        if name != ROOT.name:
            warnings.append(f"Frontmatter name ({name!r}) differs from directory name ({ROOT.name!r})")

    if not desc:
        errors.append("Frontmatter missing required field: description")
    elif len(desc) > MAX_DESC_LEN:
        errors.append(f"Frontmatter description exceeds {MAX_DESC_LEN} chars: {len(desc)}")


def validate_links_and_budgets(errors: list[str], warnings: list[str]) -> set[Path]:
    md_files = sorted(ROOT.rglob("*.md"))
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    referenced: set[Path] = {SKILL_MD.resolve()}

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        rel_src = md_file.relative_to(ROOT)

        # Check per-reference context budget so no single reference bloats loading
        if rel_src.parts[0] == "references" and len(content.splitlines()) > MAX_REF_LINES:
            warnings.append(
                f"Reference file {rel_src} has {len(content.splitlines())} lines (recommended <= {MAX_REF_LINES})"
            )

        # Strip fenced code blocks to avoid false positives on example links
        stripped = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        for raw_target in link_re.findall(stripped):
            target = raw_target.strip()
            if (
                not target
                or target.startswith(("http://", "https://", "mailto:", "#"))
                or target.startswith("<")
            ):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (md_file.parent / path_part).resolve()
            if not resolved.exists():
                errors.append(f"Broken relative link in {rel_src}: {raw_target}")
            else:
                referenced.add(resolved)

    # Ensure every file inside references/, workflows/, checklists/, templates/, examples/ is reachable
    for folder in ("references", "workflows", "checklists", "templates", "examples"):
        folder_path = ROOT / folder
        if not folder_path.exists():
            errors.append(f"Missing expected folder: {folder}/")
            continue
        for item in sorted(folder_path.rglob("*")):
            if item.is_file() and item.resolve() not in referenced:
                warnings.append(f"Unreferenced skill file (not linked from any doc): {item.relative_to(ROOT)}")

    return referenced


def validate_tokens(errors: list[str]) -> None:
    if not TOKENS_JSON.exists():
        errors.append("Missing templates/design-tokens.json")
        return
    try:
        data = json.loads(TOKENS_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in templates/design-tokens.json: {exc}")
        return

    def resolve_path(obj: dict, dotted: str) -> bool:
        cur = obj
        for part in dotted.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                return False
        return isinstance(cur, dict) and "$value" in cur

    alias_re = re.compile(r"^\{([a-zA-Z0-9_.-]+)\}$")

    def walk(node: object, path: str = "") -> None:
        if isinstance(node, dict):
            if "$value" in node:
                val = node["$value"]
                if isinstance(val, str):
                    m = alias_re.match(val)
                    if m and not resolve_path(data, m.group(1)):
                        errors.append(f"Broken token alias at {path}: {val}")
            else:
                for k, v in node.items():
                    if k.startswith("$"):
                        continue
                    walk(v, f"{path}.{k}" if path else k)

    walk(data)

    # Verify WCAG 2.2 AA contrast (>= 4.5:1) for key foreground/background token pairs
    def srgb_to_lin(c: int) -> float:
        s = c / 255.0
        return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4

    def luminance(hex_color: str) -> float:
        h = hex_color.lstrip("#")
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return 0.2126 * srgb_to_lin(r) + 0.7152 * srgb_to_lin(g) + 0.0722 * srgb_to_lin(b)

    def resolve_hex(dotted: str) -> str:
        cur: object = data
        for part in dotted.split("."):
            cur = cur[part]  # type: ignore[index]
        val = cur["$value"]  # type: ignore[index]
        m = alias_re.match(val) if isinstance(val, str) else None
        return resolve_hex(m.group(1)) if m else str(val)

    contrast_pairs = [
        ("semantic.light.text.primary", "semantic.light.bg.surface"),
        ("semantic.light.text.secondary", "semantic.light.bg.surface"),
        ("semantic.light.text.tertiary", "semantic.light.bg.canvas"),
        ("semantic.light.text.onAccent", "semantic.light.accent.primary"),
        ("semantic.light.accent.text", "semantic.light.bg.surface"),
        ("semantic.dark.text.primary", "semantic.dark.bg.surfaceRaised"),
        ("semantic.dark.text.secondary", "semantic.dark.bg.surfaceRaised"),
        ("semantic.dark.text.tertiary", "semantic.dark.bg.surfaceRaised"),
        ("semantic.dark.text.onAccent", "semantic.dark.accent.primary"),
        ("semantic.dark.accent.text", "semantic.dark.bg.surfaceRaised"),
    ]
    for fg_path, bg_path in contrast_pairs:
        fg, bg = resolve_hex(fg_path), resolve_hex(bg_path)
        l1, l2 = sorted([luminance(fg), luminance(bg)], reverse=True)
        ratio = (l1 + 0.05) / (l2 + 0.05)
        if ratio < 4.5:
            errors.append(
                f"WCAG AA contrast failure (< 4.5:1): {fg_path} ({fg}) on {bg_path} ({bg}) = {ratio:.2f}:1"
            )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    validate_frontmatter(errors, warnings)
    validate_links_and_budgets(errors, warnings)
    validate_tokens(errors)

    md_count = len(list(ROOT.rglob("*.md")))
    skill_lines = len(SKILL_MD.read_text(encoding="utf-8").splitlines()) if SKILL_MD.exists() else 0

    print(f"Skill root : {ROOT}")
    print(f"Markdown   : {md_count} files")
    print(f"SKILL.md   : {skill_lines} lines (budget <= {MAX_SKILL_LINES})")
    print(f"Errors     : {len(errors)}")
    print(f"Warnings   : {len(warnings)}")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  [WARN] {w}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  [ERR]  {e}")
        return 1

    print("\nValidation PASSED: Frontmatter, context budgets, links, DTCG aliases, and WCAG 2.2 AA contrast are all valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
