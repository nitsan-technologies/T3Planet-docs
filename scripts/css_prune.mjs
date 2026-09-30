// Remove provably dead CSS from scripts/src/custom.src.css (build tooling; scripts/ is mintignored).
//
//   node scripts/css_prune.mjs            report only
//   node scripts/css_prune.mjs --write    rewrite scripts/src/custom.src.css
//
// Needs postcss + postcss-selector-parser in the tooling dir used by
// build_perf_assets.py (T3_TOOLING_DIR, default ~/.cache/t3-docs-tooling).
//
// Only two kinds of CSS are removed:
//  1. Selectors with a t3-* class/id (our own namespace) that appears nowhere in
//     our JS, markdown or docs.json, so nothing can ever add that token.
//  2. Declarations always overridden by a later declaration of the same property
//     in a rule with the identical selector and identical @media/@supports context
//     (same or higher importance). Newer-CSS values are kept as fallbacks.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const TOOLING = process.env.T3_TOOLING_DIR || path.join(os.homedir(), ".cache", "t3-docs-tooling");
const require = createRequire(path.join(TOOLING, "package.json"));
const postcss = require("postcss");
const selectorParser = require("postcss-selector-parser");

const CSS_SRC = path.join(ROOT, "scripts", "src", "custom.src.css");
const CORPUS_FILES = [
  "scripts/src/t3-docs.js",
  "_static/t3-stats-inline.js",
  "docs.json",
];
const SKIP_DIRS = new Set([
  ".git", "node_modules", "docs-master", "workshops", "backup", "scripts", "de", "docs", "Live-docs", ".cursor",
]);
// Author utilities documented for use inside Markdown: keep even when unused today.
const KEEP_TOKENS = new Set(["t3-kv-table", "t3-note", "t3-kbd"]);
const OWN = /^t3(-|[A-Z]|$)/;
const FALLBACK_SENSITIVE = /dvh|svh|lvh|dvw|svw|lvw|color-mix|-webkit-|-moz-|\blh\b|cqw|cqh|round\(/i;

function collectMarkdown(dir, out) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!SKIP_DIRS.has(entry.name) && !entry.name.startsWith("RST Format")) collectMarkdown(path.join(dir, entry.name), out);
    } else if (/\.mdx?$/.test(entry.name)) {
      out.push(fs.readFileSync(path.join(dir, entry.name), "utf8"));
    }
  }
  return out;
}

const corpus = CORPUS_FILES.map((f) => fs.readFileSync(path.join(ROOT, f), "utf8"))
  .concat(collectMarkdown(ROOT, []))
  .join("\n");
const alive = new Map();
const tokenAlive = (t) => {
  if (!alive.has(t)) alive.set(t, KEEP_TOKENS.has(t) || corpus.includes(t));
  return alive.get(t);
};

const src = fs.readFileSync(CSS_SRC, "utf8");
const root = postcss.parse(src, { from: CSS_SRC });
const inKeyframes = (node) => node.parent && node.parent.type === "atrule" && /keyframes/i.test(node.parent.name);
const stats = { deadTokens: new Set(), selectors: 0, rules: 0, decls: 0 };

// A dead token inside :not() makes the selector match more, so it proves nothing.
function insideNot(node) {
  for (let p = node.parent; p; p = p.parent) {
    if (p.type === "pseudo" && p.value.toLowerCase() === ":not") return true;
  }
  return false;
}

function deadTokensOf(selector) {
  const dead = [];
  selectorParser((sel) => {
    sel.walk((n) => {
      if ((n.type === "class" || n.type === "id") && OWN.test(n.value) && !tokenAlive(n.value) && !insideNot(n)) {
        dead.push(n.value);
      }
    });
  }).processSync(selector);
  return dead;
}

root.walkRules((rule) => {
  if (inKeyframes(rule)) return;
  const keep = rule.selectors.filter((s) => {
    const dead = deadTokensOf(s);
    dead.forEach((t) => stats.deadTokens.add(t));
    return !dead.length;
  });
  if (keep.length === rule.selectors.length) return;
  stats.selectors += rule.selectors.length - keep.length;
  if (keep.length) rule.selectors = keep;
  else {
    rule.remove();
    stats.rules++;
  }
});

const context = (node) => {
  const parts = [];
  for (let p = node.parent; p && p.type !== "root"; p = p.parent) {
    if (p.type === "atrule") parts.unshift(`@${p.name} ${p.params.replace(/\s+/g, " ").trim()}`);
  }
  return parts.join(" | ");
};
const decls = [];
root.walkDecls((d) => {
  if (d.parent && d.parent.type === "rule" && !inKeyframes(d.parent)) decls.push(d);
});
// Covering values a browser engine rejects (it would fall back to the earlier
// declaration). Produced by the QA engine check from --pairs output.
const unsupportedIdx = process.argv.indexOf("--unsupported");
const unsupported = new Set(
  unsupportedIdx !== -1 ? JSON.parse(fs.readFileSync(process.argv[unsupportedIdx + 1], "utf8")) : []
);
const pairs = [];
const strongestLater = new Map();
for (let i = decls.length - 1; i >= 0; i--) {
  const d = decls[i];
  const key = `${context(d.parent)}||${d.parent.selector.replace(/\s+/g, " ").trim()}||${d.prop.toLowerCase()}`;
  const later = strongestLater.get(key);
  const covered = later && (later.important || !d.important);
  const laterId = later && `${d.prop.toLowerCase()}: ${later.value}`;
  if (covered && !unsupported.has(laterId) && !FALLBACK_SENSITIVE.test(later.value) && !FALLBACK_SENSITIVE.test(d.value)) {
    pairs.push({ prop: d.prop.toLowerCase(), removed: d.value, covering: later.value });
    d.remove();
    stats.decls++;
    continue;
  }
  if (!later || d.important || !later.important) strongestLater.set(key, { important: d.important, value: d.value });
}

const isEmpty = (node) => !node.nodes || node.nodes.every((n) => n.type === "comment");
root.walkRules((rule) => {
  if (isEmpty(rule)) {
    rule.remove();
    stats.rules++;
  }
});
root.walkAtRules((at) => {
  if (/^(media|supports|container|layer)$/i.test(at.name) && at.nodes && isEmpty(at)) at.remove();
});

const out = root.toString();
console.log(
  JSON.stringify({
    bytesBefore: src.length,
    bytesAfter: out.length,
    removedSelectors: stats.selectors,
    removedRules: stats.rules,
    removedDeclarations: stats.decls,
    deadTokens: [...stats.deadTokens].sort(),
  }, null, 1)
);
const pairsIdx = process.argv.indexOf("--pairs");
if (pairsIdx !== -1) fs.writeFileSync(process.argv[pairsIdx + 1], JSON.stringify(pairs, null, 1));
if (process.argv.includes("--write")) fs.writeFileSync(CSS_SRC, out);
