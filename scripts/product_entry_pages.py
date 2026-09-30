#!/usr/bin/env python3
"""Product entry pages: clicking a product opens its first doc page, not its overview.

Source of truth is `docs.json`: for every product group (a group with a `root`
inside the AI / Templates / Extensions sections) the entry page is the first
navigation page after the root, e.g. `ExtNsT3AF/Index` -> `ExtNsT3AF/Introduction/Index`.
Products without further pages keep their root.

Usage:
  python3 scripts/product_entry_pages.py          # rewrite product links in hubs + footer
  python3 scripts/product_entry_pages.py --check  # exit 1 if any product link is stale
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_JSON = ROOT / "docs.json"
DOCS_BASE = "/en/latest"
PRODUCT_SECTIONS = {"AI Extensions", "Templates & Themes", "TYPO3 Extensions"}
LINK_FILES = [
    "index.md",
    "AIFoundationExtensions/Index.md",
    "AllTemplates/Index.md",
    "AllExtensions/Index.md",
    "docs.json",
]


def _first_page(pages: list, root: str) -> str | None:
    for page in pages:
        if isinstance(page, str):
            if page != root:
                return page
        elif isinstance(page, dict):
            if page.get("root") and page["root"] != root:
                return page["root"]
            found = _first_page(page.get("pages", []), root)
            if found:
                return found
    return None


def product_entry_pages(docs: dict | None = None) -> dict[str, str]:
    """Map product root route -> entry route (both without base, e.g. `/ExtNsT3AF/Index`)."""
    docs = docs or json.loads(DOCS_JSON.read_text(encoding="utf-8"))
    entries: dict[str, str] = {}

    def walk(node, section: str | None) -> None:
        if isinstance(node, list):
            for item in node:
                walk(item, section)
            return
        if not isinstance(node, dict):
            return
        group = node.get("group")
        if group and node.get("root") and section in PRODUCT_SECTIONS:
            entry = _first_page(node.get("pages", []), node["root"])
            if entry:
                entries["/" + node["root"]] = "/" + entry
            return
        child_section = group if group else section
        for value in node.values():
            if isinstance(value, (list, dict)):
                walk(value, child_section)

    walk(docs.get("navigation", {}), None)
    return entries


def js_entry_list(entries: dict[str, str] | None = None) -> list[str]:
    """Entry routes for the sidebar script; the product root is `/<first segment>/Index`."""
    entries = entries or product_entry_pages()
    for root, entry in entries.items():
        if root != "/" + entry.split("/")[1] + "/Index":
            raise ValueError(f"entry {entry} is not inside product root {root}")
    return sorted(entries.values())


def _rewrite(text: str, entries: dict[str, str]) -> str:
    def repl(match: re.Match) -> str:
        route = match.group(2)
        return match.group(1) + DOCS_BASE + entries.get(route, route) + match.group(3)

    return re.sub(r'((?:\bhref=|"href":\s*)")' + re.escape(DOCS_BASE) + r'(/[^"#?]+)(")', repl, text)


def sync_product_links(check: bool = False) -> list[str]:
    entries = product_entry_pages()
    changed = []
    for rel in LINK_FILES:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        new = _rewrite(text, entries)
        if new != text:
            changed.append(rel)
            if not check:
                path.write_text(new, encoding="utf-8")
    return changed


if __name__ == "__main__":
    check = "--check" in sys.argv
    changed = sync_product_links(check=check)
    print(f"{len(product_entry_pages())} product entry pages")
    if check:
        print("stale: " + (", ".join(changed) if changed else "none"))
        sys.exit(1 if changed else 0)
    print("updated: " + (", ".join(changed) if changed else "none"))
