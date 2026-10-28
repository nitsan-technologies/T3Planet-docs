/**
 * Mintlify injects U+200B (zero-width space) into heading permalink anchors
 * ("Navigate to header"). That character is not in our Markdown source, but it
 * shows up in the rendered HTML and in copied heading text.
 *
 * This script strips common zero-width characters from headings after render
 * and on client-side navigation.
 */
(function () {
  "use strict";
  if (window.__t3StripHeadingZw) return;
  window.__t3StripHeadingZw = true;

  var ZW = /[\u200B\u200C\u200D\uFEFF\u2060]/g;

  function stripNode(root) {
    if (!root || !root.querySelectorAll) return;
    var headings = root.querySelectorAll("h1, h2, h3, h4, h5, h6");
    for (var i = 0; i < headings.length; i++) {
      stripTree(headings[i]);
    }
  }

  function stripTree(el) {
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
    var node;
    while ((node = walker.nextNode())) {
      if (node.nodeValue && ZW.test(node.nodeValue)) {
        node.nodeValue = node.nodeValue.replace(ZW, "");
      }
    }
  }

  function run() {
    var article =
      document.querySelector("article") ||
      document.querySelector("main") ||
      document.body;
    stripNode(article);
  }

  function schedule() {
    run();
    // Mintlify hydrates / swaps content after first paint
    setTimeout(run, 0);
    setTimeout(run, 250);
    setTimeout(run, 1000);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", schedule);
  } else {
    schedule();
  }

  // Client-side route changes
  var pushState = history.pushState;
  if (typeof pushState === "function") {
    history.pushState = function () {
      var ret = pushState.apply(this, arguments);
      schedule();
      return ret;
    };
  }
  window.addEventListener("popstate", schedule);

  try {
    var mo = new MutationObserver(function () {
      run();
    });
    mo.observe(document.documentElement, { childList: true, subtree: true });
  } catch (e) {}
})();
