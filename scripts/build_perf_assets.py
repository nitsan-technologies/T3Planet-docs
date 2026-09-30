#!/usr/bin/env python3
"""Build published Mintlify assets.

Mintlify inlines `custom.css` and every `_static/*.js` into the HTML RSC
payload on every page. Keep published files tiny:

- Source JS lives in `scripts/src/t3-docs.js` (NOT under `_static/`)
- Published JS is only `_static/t3-docs.min.js` (+ tiny stats inline)
- `custom.css` is minified in place from `custom.src.css` when present
- Minifier: pinned esbuild from TOOLING_DIR (auto-installed); `--legacy-minify`
  or a missing npm falls back to the conservative regex minifier
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Mintlify publishes every *.js in the repo, so build tooling (node_modules)
# must live outside it. Override with T3_TOOLING_DIR or T3_ESBUILD.
TOOLING_DIR = Path(os.environ.get("T3_TOOLING_DIR", Path.home() / ".cache" / "t3-docs-tooling"))
ESBUILD_VERSION = "0.28.1"
BROWSER_TARGETS = "chrome100,edge100,firefox100,safari15"
CSS_PUB = ROOT / "custom.css"
CSS_SRC = ROOT / "scripts" / "src" / "custom.src.css"
JS_IN = ROOT / "scripts" / "src" / "t3-docs.js"
# Legacy fallback while migrating
JS_LEGACY = ROOT / "_static" / "t3-docs.js"
JS_OUT = ROOT / "_static" / "t3-docs.min.js"


def _strip_js_line_comment(line: str) -> str:
    """Remove // comments without touching // inside strings or URLs (://)."""
    in_single = False
    in_double = False
    escaped = False
    i = 0
    while i < len(line) - 1:
        ch = line[i]
        nxt = line[i + 1]
        if escaped:
            escaped = False
            i += 1
            continue
        if ch == "\\" and (in_single or in_double):
            escaped = True
            i += 1
            continue
        if not in_single and not in_double:
            if ch == "'" :
                in_single = True
            elif ch == '"':
                in_double = True
            elif (
                ch == "/"
                and nxt == "/"
                and (i == 0 or line[i - 1] not in (":", "\\"))
            ):
                # Skip :// URLs and regexes like /^\// (backslash before slash)
                return line[:i].rstrip()

            elif ch == "/" and nxt == "*":
                # block comments handled globally; leave alone here
                pass
        else:
            if in_double and ch == '"':
                in_double = False
            elif in_single and ch == "'":
                in_single = False
        i += 1
    return line


def minify_js(text: str) -> str:
    text = re.sub(r"/\*[\s\S]*?\*/", "", text)
    text = "\n".join(_strip_js_line_comment(line) for line in text.splitlines())
    text = re.sub(r"\n\s+", "\n", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


def minify_css(text: str) -> str:
    """Conservative CSS minify — safe for Mintlify-inlined custom.css.

    Do not strip spaces around +/− (breaks calc()) or inside strings.
    """
    text = re.sub(r"/\*[\s\S]*?\*/", "", text)
    text = re.sub(r"\s+", " ", text)
    # Safe separators only — never + or - (calc / custom-idents).
    # Keep whitespace before ":" — in selectors it is a descendant combinator (`td :is(...)`).
    text = re.sub(r"\s*([{};,\>])\s*", r"\1", text)
    text = re.sub(r":\s+", ":", text)
    text = re.sub(r";}", "}", text)
    text = text.replace(" !important", "!important")
    return text.strip()


def find_esbuild(install: bool = True) -> str | None:
    """Return the pinned esbuild binary, installing it into TOOLING_DIR if needed."""
    explicit = os.environ.get("T3_ESBUILD")
    if explicit:
        return explicit
    binary = TOOLING_DIR / "node_modules" / ".bin" / "esbuild"
    if not binary.exists() and install and shutil.which("npm"):
        TOOLING_DIR.mkdir(parents=True, exist_ok=True)
        pkg = TOOLING_DIR / "package.json"
        if not pkg.exists():
            pkg.write_text('{"name":"t3-docs-tooling","private":true}\n', encoding="utf-8")
        subprocess.run(
            ["npm", "install", "--no-audit", "--no-fund", f"esbuild@{ESBUILD_VERSION}"],
            cwd=TOOLING_DIR,
            capture_output=True,
            text=True,
        )
    if not binary.exists():
        return None
    version = subprocess.run([str(binary), "--version"], capture_output=True, text=True).stdout.strip()
    if version != ESBUILD_VERSION:
        print(f"Warning: esbuild {version} found, pinned {ESBUILD_VERSION}", file=sys.stderr)
    return str(binary)


def esbuild_minify(esbuild: str, text: str, loader: str) -> str:
    target = "es2017" if loader == "js" else BROWSER_TARGETS
    result = subprocess.run(
        [esbuild, f"--loader={loader}", "--minify", f"--target={target}", "--charset=utf8", "--legal-comments=none"],
        input=text,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"ERROR: esbuild failed for {loader}:\n{result.stderr}")
    return result.stdout.strip()


PRODUCT_ENTRY_PLACEHOLDER = '"__T3_PRODUCT_ENTRY_PAGES__"'


def inject_product_entry_pages(js: str) -> str:
    """Replace the sidebar placeholder with product entry routes from docs.json."""
    import json

    from product_entry_pages import js_entry_list

    if PRODUCT_ENTRY_PLACEHOLDER not in js:
        raise SystemExit(f"ERROR: {PRODUCT_ENTRY_PLACEHOLDER} missing from JS source")
    return js.replace(PRODUCT_ENTRY_PLACEHOLDER, json.dumps(js_entry_list(), separators=(",", ":")))


def main() -> None:
    dry = "--dry-run" in sys.argv

    js_path = JS_IN if JS_IN.exists() else JS_LEGACY
    if not js_path.exists():
        print(f"ERROR: missing JS source at {JS_IN}", file=sys.stderr)
        sys.exit(1)

    # Prefer editable source; bootstrap custom.src.css once from current custom.css
    if CSS_SRC.exists():
        css_raw = CSS_SRC.read_text(encoding="utf-8")
    else:
        css_raw = CSS_PUB.read_text(encoding="utf-8")
        if not dry:
            CSS_SRC.write_text(css_raw, encoding="utf-8")
            print(f"Bootstrapped {CSS_SRC.name} from custom.css")

    js_raw = js_path.read_text(encoding="utf-8")
    js_full = inject_product_entry_pages(js_raw)
    esbuild = None if "--legacy-minify" in sys.argv else find_esbuild()
    if esbuild:
        css_min = esbuild_minify(esbuild, css_raw, "css")
        js_min = esbuild_minify(esbuild, js_full, "js")
        print(f"Minifier: esbuild {ESBUILD_VERSION}")
    else:
        print("Warning: esbuild unavailable, using the conservative fallback minifier", file=sys.stderr)
        css_min = minify_css(css_raw)
        js_min = minify_js(js_full)

    print(f"CSS: {len(css_raw)} -> {len(css_min)} bytes ({100 - len(css_min)*100//max(len(css_raw),1)}% smaller)")
    print(f"JS:  {len(js_raw)} -> {len(js_min)} bytes ({100 - len(js_min)*100//max(len(js_raw),1)}% smaller) from {js_path.relative_to(ROOT)}")

    if not dry:
        CSS_PUB.write_text(css_min + "\n", encoding="utf-8")
        JS_OUT.write_text(js_min, encoding="utf-8")
        # Ensure source is never published under _static (Mintlify inlines all *.js there)
        if JS_LEGACY.exists() and JS_IN.exists():
            JS_LEGACY.unlink()
            print("Removed published _static/t3-docs.js (source-only under scripts/src/)")
        print(f"Wrote {CSS_PUB.name} + {JS_OUT.name}")
        # Fail closed: never publish JS that does not parse.
        check = subprocess.run(
            ["node", "--check", str(JS_OUT)],
            capture_output=True,
            text=True,
        )
        if check.returncode != 0:
            print(check.stderr, file=sys.stderr)
            raise SystemExit(f"ERROR: {JS_OUT.name} failed node --check")

        try:
            from compute_doc_stats import write_stats_json

            write_stats_json()
            print("Regenerated t3-stats-inline.js")
        except Exception as exc:
            print(f"Warning: stats inline not regenerated ({exc})")


if __name__ == "__main__":
    main()
