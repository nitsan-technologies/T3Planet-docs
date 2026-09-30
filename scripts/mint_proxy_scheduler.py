"""Upstream scheduling for mint_cache_proxy: one compile gate + one warm queue.

mint dev wedges under parallel MDX/RSC compiles, so page compiles are serialized.
Interactive requests must never wait behind background warm-up: after a cache
purge every warm is a cold compile of several seconds, and a flood of them made
the first real page load wait up to two minutes.
"""
from __future__ import annotations

import threading
import time
from collections import deque
from typing import Callable


class CompileGate:
    """Limits concurrent mint compiles; interactive callers always go first.

    Background callers only start when no interactive caller is waiting and no
    interactive compile happened within ``quiet_sec`` (a page load is a burst of
    HTML + RSC requests; a warm must not slip into the gaps of that burst).
    A compile that already runs cannot be preempted.
    """

    def __init__(self, capacity: int = 1, quiet_sec: float = 2.0) -> None:
        self._cond = threading.Condition()
        self._capacity = max(1, capacity)
        self._active = 0
        self._users_waiting = 0
        self._last_user = 0.0
        self._quiet_sec = quiet_sec

    def acquire_user(self) -> None:
        with self._cond:
            self._users_waiting += 1
            try:
                while self._active >= self._capacity:
                    self._cond.wait()
            finally:
                self._users_waiting -= 1
            self._active += 1
            self._last_user = time.monotonic()

    def acquire_background(self, timeout: float | None = None) -> bool:
        deadline = None if timeout is None else time.monotonic() + timeout
        with self._cond:
            while True:
                free = self._active < self._capacity and self._users_waiting == 0
                quiet_left = self._quiet_sec - (time.monotonic() - self._last_user)
                if free and quiet_left <= 0:
                    self._active += 1
                    return True
                wait = quiet_left if free else None
                if deadline is not None:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        return False
                    wait = remaining if wait is None else min(wait, remaining)
                self._cond.wait(wait)

    def release(self, *, user: bool) -> None:
        with self._cond:
            self._active -= 1
            if user:
                self._last_user = time.monotonic()
            self._cond.notify_all()


class WarmQueue:
    """Single background worker that warms routes one at a time.

    Browsing intent (neighbors, hover) is served newest-first and capped, so
    stale intent from pages the user already left is dropped. Hub catalog warms
    run only when no intent is queued. Duplicates are ignored, routes that are
    already cached are skipped, and a user request for the route currently being
    warmed can wait for that warm instead of compiling it a second time.
    """

    def __init__(
        self,
        gate: CompileGate,
        warm: Callable[[str], None],
        is_fresh: Callable[[str], bool],
        max_intent: int = 12,
    ) -> None:
        self._gate = gate
        self._warm = warm
        self._is_fresh = is_fresh
        self._max_intent = max_intent
        self._cond = threading.Condition()
        self._intent: deque[str] = deque()
        self._hubs: deque[str] = deque()
        self._force: set[str] = set()
        self._inflight: dict[str, threading.Event] = {}
        self._thread: threading.Thread | None = None

    def start(self) -> None:
        with self._cond:
            if self._thread is None:
                self._thread = threading.Thread(target=self._run, name="t3-warm", daemon=True)
                self._thread.start()

    def push(self, path: str, *, hub: bool = False, force: bool = False) -> None:
        with self._cond:
            if path in self._inflight:
                return
            queued = path in self._intent or path in self._hubs
            if force:
                self._force.add(path)
            if hub:
                if not queued:
                    self._hubs.append(path)
            else:
                if path in self._hubs:
                    self._hubs.remove(path)
                if path in self._intent:
                    self._intent.remove(path)
                self._intent.appendleft(path)
                while len(self._intent) > self._max_intent:
                    self._force.discard(self._intent.pop())
            self._cond.notify()

    def wait_inflight(self, path: str, timeout: float) -> bool:
        """Block while ``path`` is being warmed. Returns True if a warm was awaited."""
        with self._cond:
            event = self._inflight.get(path)
        return bool(event and event.wait(timeout))

    def depth(self) -> dict[str, int]:
        with self._cond:
            return {"intent": len(self._intent), "hubs": len(self._hubs), "inflight": len(self._inflight)}

    def _wait_for_work(self) -> None:
        with self._cond:
            while not (self._intent or self._hubs):
                self._cond.wait()

    def _claim(self) -> str | None:
        """Pop the newest route that still needs a compile (caller holds the gate)."""
        while True:
            with self._cond:
                if not (self._intent or self._hubs):
                    return None
                path = self._intent.popleft() if self._intent else self._hubs.popleft()
                force = path in self._force
                self._force.discard(path)
            if force or not self._is_fresh(path):
                with self._cond:
                    self._inflight[path] = threading.Event()
                return path

    def _done(self, path: str) -> None:
        with self._cond:
            event = self._inflight.pop(path, None)
        if event:
            event.set()

    def _run(self) -> None:
        while True:
            self._wait_for_work()
            self._gate.acquire_background()
            path = None
            try:
                path = self._claim()
                if path:
                    self._warm(path)
            except Exception as exc:  # worker must survive any single failure
                print(f"[cache-proxy] warm failed {path}: {exc}", flush=True)
            finally:
                self._gate.release(user=False)
                if path:
                    self._done(path)
