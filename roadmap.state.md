# 🗺️ AI Mastery Roadmap — State File (v2)

> Last updated: July 15, 2026
> This file is the single source of truth for roadmap progress.
> Update this after every session. Paste into new Claude accounts to resume.
> **v2 redesign (Jun 3, 2026):** rebalanced to a TRUE ~16-month critical path, deploy-from-Phase-1 reliability spine, gentler gamification. Past progress is untouched — only the path forward changed.

---

## 🧭 Philosophy (read first)

- **Mastery over speed.** ~16 months is the budget, not a deadline. Goal = a *reliable, elite* AI + backend engineer strong on **deployment/production**.
- **The DONE law:** *If it isn't in Git with a passing test, it doesn't exist. If it isn't deployed at a public URL with a documented baseline beaten, it isn't DONE.* (Ported from the Flutter instinct: a feature isn't done until it's signed and on a device.)
- **Ship every phase.** A deployed artifact escalates in production-realism each phase (Gradio → Dockerized FastAPI → traced RAG/agent → monitored full-stack flagship).
- **Optional ≠ skippable-forever, but never a blocker.** Deep-learning-from-scratch and fine-tuning are trophy-gated enrichment, off the critical path. If a phase slips, optional enrichment is dropped first — never the hireable core.
- **Resource-first, just-in-time.** Watch/read the one pinned resource, then build. No concept introduced without a resource; no tool introduced without a measured need.

---

## 📊 Current Status

> ⚠️ **PIVOT 2026-07-09 → build-first.** Day 23 flipped the plan from bottom-up fundamentals to **top-down building** (ship real AI-feeling apps NOW; backfill fundamentals just-in-time when a build demands them). 🥉 First Token popped (first LLM API call). The **Today** / **sub-goal** cells and the Phase archive below still describe the OLD bottom-up plan in places — a full rewrite is PENDING. Trust this banner + the Day 23 row over any stale cell.

| Field | Value |
|-------|-------|
| **Current Day** | 29 |
| **Rank** | E |
| **XP** | 775 |
| **Phase** | 1 |
| **Today** | **Day 29 ✅ DONE — 🥉 PR Author + streaming LIVE in production** (Wed Jul 15 IST) — **closed Day 28's open loop.** The streaming generator existed only on his laptop while the public URL still served the Day-25 one-shot bot — so by his own DONE law, Day 28 *wasn't done*. Shipped it through his **first branch → first PR → first merge**: branch `streaming-deploy` → ported the generator into `phase1/week4/deploy/app.py` (**deleted the now-dead `aiBot`**, **kept** the Day-27 `0.0.0.0`+`$PORT` launch line — both decisions made unaided) → verified LOCALLY first → PR #1 → `main`. **Verified LIVE at https://gemini-chatbot-tw9q.onrender.com/ — types live AND remembers his name, in the cloud.** ⭐ **Empirical win:** every source said "does Render's proxy buffer Gradio's SSE stream?" was **UNDOCUMENTED/UNKNOWN** — his deploy answers it: **it does not buffer.** He owns that fact now. **Bonus bug caught by adversarial review + fixed:** `print("(debug)", e)` was **invisible on Render** — Python **line-buffers to a TTY but block-buffers (128KB) to a pipe**, so his debug notes sat unsent and died at spin-down while uvicorn's *stderr* logs looked healthy → he'd have concluded "no exception ever fired." Fixed with `flush=True`; **chose explicit-in-repo over Render's `PYTHONUNBUFFERED=1`** dashboard config (= "works on my Render", the same disease as "works on my machine"). Also **verified by a skeptic:** his `gr.State` is genuinely **per-session under concurrency** — no cross-visitor conversation leak on the public URL (the Day-25 "never use a global" instinct holding up). **Two honest misses — logged, not hidden:** (1) he **merge-committed instead of squash-merging** (hit the default button; `main` now carries a 2-parent bubble AND both messy commits, incl. the "Created a branch…" one — left in place deliberately, rewriting pushed history is the worse sin); (2) the PR body still has **What but no Why / How-tested** despite having the evidence in hand. **The real rep was the PR title** — 4 rounds, ending in him asking for it outright: *"If merged, this PR will ___"* is the test; hedges like *"change the mechanics of how"* carry **zero information**; and the title becomes the commit subject on `main` **forever**. **Next — Day 30:** 🥉 **First Model** (NumPy logistic regression beats a majority-class baseline) — resumes the parked Phase-1 core. |
| **Today (archived Day 28)** | **Day 28 ✅ DONE — streaming chatbot (live token typing)** (Tue Jul 14 IST) — made the local twin of the deployed bot **type word-by-word**, like a real AI product. Turned Day-25's one-shot `random_response` into a **Python generator**: `client.interactions.create(..., stream=True)` returns an **event stream**; he grabs the new interaction id from the first `interaction.created` event, accumulates `step.delta` text, and **`yield`s the growing string + id each step** so Gradio repaints the bubble live. Kept per-session memory via `gr.State` — **stream and memory are independent** (one `stream=True` flag, no rewrite of the `previous_interaction_id` logic). **Verified live locally:** it types as it thinks AND still remembers his name across turns. **The real win = the debugging loop:** wrote it, hit a **blank-bubble** bug (wrong event-type string `"interaction"` → `"step.delta"`, so the accumulate branch never fired), then a **sleeper** (`return` inside a generator silently swallows the value → must `yield`) — diagnosed both from evidence and iterated twice to green. New file `phase1/week4/day28.py`; gitignored the `.gradio/` cache; commit `b7cb99c` on `main`. **Context this session:** briefly explored a personal **RAG-over-a-Gujarati-Granth** idea → parked as a future **Phase-3 flagship** (verified feasible & $0 — Gemini reads Gujarati scans, cross-lingual embeddings handle any-language questions; gated on **community permission** to digitize the edition). Also had an honest **"am I actually growing or just prompting ideas?"** gut-check — answer landed: the write→break→read-the-evidence→fix loop he ran today **is** the engineering muscle. **Next — Day 29:** loop back toward 🥉 **First Model** (NumPy logistic regression) OR pop 🥉 **PR Author** by shipping the streaming redeploy via a branch + PR-to-self. |
| **This week's sub-goal** | **Week 5 (Days 29–35) — deploy arc CLOSED, Phase-1 core resumes:** 🥉 **PR Author** + streaming shipped LIVE to production (29) ✅ → **🥉 First Model** (NumPy logistic regression beats a majority-class baseline — the parked Phase-1 core, un-parked) → 🥉 **From Raw** micro-pops (pandas on a real messy CSV: First Merge/Join · Killed the NaNs · Leak-Free Split) → **Sunday 33 = mandatory rest**. *Week-4 recap: token (23) → memory (24) → browser UI (25) → public deploy (27) → live streaming (28) → shipped-via-PR (29). The whole build-first arc is now closed end-to-end: an AI app anyone can load, that types as it thinks, remembers per-visitor, and ships through a reviewed PR.* Next infra tool: none — Day 30 is deliberately **zero new tools** (NumPy + pytest only) to keep the concept lift clean. |
| **Streak** | 6 (Days 23–25, 27, 28, 29 ✅; Sundays 26 = neutral rest). Six build-first days: token → memory → browser UI → public deploy → live streaming → shipped-via-PR. Notably **Day 29 was a "finish it properly" day, not a new-toy day** — he closed his own open loop instead of chasing the next feature. That's the harder muscle. |
| **Streak-Freeze tokens** | 1 available (one refilled ~Jul 12, a month after the Day-19 spend; the second refills ~mid-Aug). Thin buffer restored — don't spend it casually. |
| **Start Date** | May 25, 2026 |
| **Next trophy in sight** | 🥉 **PR Author — EARNED (Day 29)** *(with an honest asterisk: merge-committed, not squash-merged; body had What but no Why/How-tested — the bar for PR #2)*. **Next: 🥉 First Model** (Day 30) — NumPy logistic regression beats a majority-class baseline. Also live and repeatable nearby: 🥉/🥈 **Baseline Beaten** (pops the same day First Model does, if the baseline is documented) and 🥉/🥈 **Bug Bounty** (close a bug with a regression test written FIRST — the Day-29 stdout-buffering bug would have qualified if he'd tested it first, worth remembering). ≤3-day cadence: healthy. |

> Surface to yourself only the **next trophy + this week's sub-goal**. Phase-week ranges below are for planning, not your daily view (you think in days).

---

## ✅ Days Completed

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Python setup, variables, data types, first functions | ✅ Done |
| Day 2 | Data structures (list/tuple/set/dict) + mini tokenizer | ✅ Done |
| Day 3 | Comprehensions + Two Sum (LeetCode) + tokenizer refactor | ✅ Done |
| Day 4 | OOP: Vector, Dataset, Layer/LinearLayer/ReluLayer classes | ✅ Done |
| Day 5 | Functions advanced (default params, *args, **kwargs, scope) | ✅ Done |
| Day 6 | String methods + Week 1 Text Analyzer project | ✅ Done |
| Day 7 | Sunday — reflection, paper, post | ✅ Done |
| Day 8 | Modules & imports (math_utils, standard library) | ✅ Done |
| Day 9 | SKIPPED (Tue Jun 2 IST) — −25 XP applied (a Streak-Freeze token would now absorb this) | ⚠️ Skipped |
| Day 10 | Error handling + File I/O | ✅ Done (Wed Jun 3 IST) |
| Day 11 | **Harden your own code** (fixed day4 crash + dead `name` param + `__main__` guard; seeded shuffle on `Dataset.split`; first pytest) | ✅ Done (Thu Jun 4 IST) |
| Day 12 | Finish hardening: `safe_divide`/`safe_int` **raise** (dead try/except removed) + regression tests (`test_divide`/`test_int`) + first **Hypothesis property test** (`test_split_conserves`, conservation law) | ✅ Done (Fri Jun 5 IST) |
| Day 13 | Testing as design: parametrized `safe_divide` (happy-path rows) + own `pytest.raises` test for ZeroDivisionError + **first fixture** (`data_set` builds & injects a `Dataset`) | ✅ Done (Sat Jun 6 IST) |
| Day 14 | **Sunday — TRUE rest day** (policy change: Sundays are now zero-task. Pre-NumPy pulse done: energy 7.5; concepts solid; real gap = syntax-recall fluency → fix with typing reps + syntax Anki) | ✅ Rest (Sun Jun 7 IST) |
| Day 15 | **NumPy first-contact**: 3B1B vectors (ch.1) → `ndarray` from a list → vectorized ReLU `np.maximum(0, c)` replacing a Python loop (**167× faster**, documented baseline) + first **uv lockfile** (`pyproject.toml` + `uv.lock`, numpy 2.4.6). Self-debugged a timestamp-vs-duration timing bug. 🥉 Vectorized + 🥉 Clean Tree | ✅ Done (Mon Jun 8 IST) |
| Day 16 | **NumPy reductions → vectorized MSE loss**: `errors ** 2` (scalar-broadcast) → `.mean()` collapses the whole error array to one number (19.75), zero loops; cleaned a redundant `np.array()` re-wrap (NumPy op in → `ndarray` out). + **gradient-descent intuition** (3B1B ch.2: blindfolded-hiker / cost surface; slope = `dL/dw`, step opposite it; caught local-vs-global minima). No new trophy — sets up 🥉 Gradient (Day 17). | ✅ Done (Tue Jun 9 IST) |
| Day 17 | **Hand-rolled single-weight gradient descent**: model `pred = w·x`; finite-difference slope `(loss(w+ε) − loss(w)) / ε` (rise÷run, ε = a tiny *chosen* nudge); update `w = w − lr·slope` (minus × negative = step OPPOSITE the slope — the previously-fuzzy step, now solid); 50-iter loop converged `w: 0 → ~2`, loss `30.0 → ~0`, slope auto-flattened toward 0 (self-braking). Caught that w approaches the true weight asymptotically (never exactly) — fine, loss negligible; test asserts `abs(w−2) < 0.01`, never `== 2`. 🥉 Gradient | ✅ Done (Wed Jun 10 IST) |
| Day 18 | **Analytic gradient via the chain rule**: replaced Day-17's finite-difference slope with the *exact* derivative `grad(w) = (2 * x * errors).mean()`, derived by hand (chain rule = multiply each step's *rate*: `w·x`→`×x`, `−target`→`×1`, `error²`→`×(2·error)` via the power rule/square-strips). Verified analytic == ε-slope (both −30 at w=0), ran the 50-iter loop → `w → 1.9994`, gradient self-braked to ~0. Caught that a *multiplier is a rate, not the line's output* (the `0.0` bug = used `pred` where the rate is `x`). Tightened a loose range assert into a real tolerance tripwire (`abs(grad(0)+30)<0.01`). Realized the update step needs only the derivative, not the loss value (so `loss()` was deletable today, unlike Day 17). Worked through a real mid-session demotivation wall. No new trophy (analytic-gradient micro-pop). | ✅ Done (Thu Jun 11 IST) |
| Day 19 | **Frozen** — missed; first Streak-Freeze token spent → miss absorbed, streak preserved, no XP penalty | 🧊 Frozen (Fri Jun 12 IST) |
| Day 20 | **Frozen** — missed; second Streak-Freeze token spent → absorbed, streak preserved | 🧊 Frozen (Sat Jun 13 IST) |
| Day 21 | **Sunday — TRUE rest day** — mandatory zero-task rest; streak-neutral, no XP | ✅ Rest (Sun Jun 14 IST) |
| Day 22 | **Re-entry: the learning-rate landscape** — re-ran Day-18 code green after a 3-day gap (read the convergence story off raw numbers cold), then turned a "don't-feel-like-it" low into a self-driven experiment mapping lr **too-small** (0.01 → crawl up from one side, never crosses 2) / **just-right** (0.1 → lands on 2 to ~13 dp) / **too-big** (2.0 → overshoots, bounces *outward*, diverges to `~1e73` → `nan`). The Day-18 tolerance assert `abs(w−2)<0.01` **correctly tripped** on the diverged run — a test caught a broken training loop. No new file (exploration of existing `day18.py`); restored lr → green. | ✅ Done (Mon Jun 15 IST) |
| Day 23 | **Re-entry + PIVOT to build-first → 🥉 First Token**: after a ~1-month gap, diagnosed that the bottom-up grind wasn't motivating him; flipped to top-down build-first (ship AI apps now, backfill fundamentals just-in-time) — he chose it. Then shipped the first brick: a **working LLM API call from Python** (Google AI Studio free tier, `google-genai`, `gemini-3.5-flash`) — an AI answered his own code (`"AI learns from data, finds patterns, and makes predictions."`). Stored the API key as an env var (first secrets lesson; repo is public). First LLM API call = 🥉 First Token, a Phase-3 trophy pulled ~8 months forward. | ✅ Done (Thu Jul 9 IST) |
| Day 24 | **First interactive chatbot (memory + error shield)**: turned Day-23's one-shot call into a live multi-turn CLI chat loop that **remembers across turns** (Interactions API + `previous_interaction_id`). Learned **3 production lessons by hitting real errors** — per-project quotas (new keys ≠ new quota), model selection by free-tier cost/limit (`gemini-3.5-flash` → `gemini-3.1-flash-lite`), and model-ID churn (a 404-retired model → check the live models page). Then fixed **2 self-inflicted bugs** that cemented fundamentals: *local vars don't leak to the caller* (return-and-catch the id), and *all return paths must share one shape* (a 1-vs-2-tuple mismatch crashed the 429 handler; proven with a runnable repro). New file `phase1/week4/day24.py`. | ✅ Done (Fri Jul 10 IST) |
| Day 25 | **First browser chatbot (Gradio + per-session memory)** — wrapped the Day-24 `aiBot` in `gr.ChatInterface` on localhost; threaded `previous_interaction_id` through a `gr.State(None)` via `additional_inputs`+`additional_outputs` (per-session, not a global). Cracked *a component passes its value, not itself*; re-fixed the Day-24 "return-it, don't-stash-a-local" bug in the Gradio wiring. Installed Gradio 6.20 (`uv add`, clean on the 3.14 pin). Verified live — it remembered his name across turns. New file `phase1/week4/day25.py`. | ✅ Done (Sat Jul 11 IST) |
| Day 26 | **Sunday — TRUE rest day** — mandatory zero-task rest; streak-neutral, no XP | ✅ Rest (Sun Jul 12 IST) |
| Day 27 | **🥉 First Deploy — first LIVE public app**: deployed the Day-25 Gradio chatbot to a **Render** free Web Service at a public URL (https://gemini-chatbot-tw9q.onrender.com/); verified in the cloud that it replies AND remembers across turns. **HF Spaces paywalled Gradio (~Jul 8–9, PRO-only) → pivoted to Render.** Built a self-contained `deploy/app.py` (inlined `aiBot`, dropped the cross-file import; bound `0.0.0.0` + `int(os.environ.get("PORT",7860))`) + pinned `requirements.txt`; grabbed a temporary `*.gradio.live` share link first. Cemented tunnel-vs-host, `0.0.0.0` bind-vs-destination, `$PORT` injection, env-var secrets, requirements pinning. | ✅ Done (Mon Jul 13 IST) |
| Day 28 | **Streaming chatbot — live token typing** — turned Day-25's one-shot `random_response` into a **generator**: `interactions.create(..., stream=True)` → grab the id from the `interaction.created` event, accumulate `step.delta` text, `yield` the growing string + id each step so Gradio repaints live; kept per-session `gr.State` memory (stream + memory independent). Fixed **two self-found bugs** (wrong event-type string `"interaction"`→`"step.delta"` = blank bubble; `return` vs `yield` inside a generator). Verified: types live + remembers name across turns. New file `phase1/week4/day28.py`, `.gradio/` gitignored, commit `b7cb99c`. | ✅ Done (Tue Jul 14 IST) |
| Day 29 | **🥉 PR Author — shipped streaming to production via his first branch + PR** — closed Day 28's open loop (streaming lived only on his laptop; the public URL still served the one-shot bot = not DONE by his own law). First `git switch -c` (`streaming-deploy`) → ported the generator into `phase1/week4/deploy/app.py` (**deleted dead `aiBot`**, **kept** the `0.0.0.0`+`$PORT` launch — unaided) → verified locally → **PR #1** → merged → **verified LIVE: types live + remembers his name in the cloud**. Answered an **undocumented** question empirically: **Render does NOT buffer Gradio's SSE stream.** Caught+fixed a real cloud-only bug: `print()` **block-buffers to a pipe** (128KB) vs line-buffers to a TTY → debug output invisible on Render → `flush=True`. Skeptic-verified `gr.State` is per-session under concurrency. Honest misses: **merge-committed not squashed**; PR body still lacked Why/How-tested. | ✅ Done (Wed Jul 15 IST) |

---

## 🧠 LeetCode Progress

| Problem | Difficulty | Status |
|---------|------------|--------|
| Two Sum | Easy | ✅ Solved |

> DSA = interview hygiene only: ~1 pattern-first NeetCode problem/week toward Blind 75 across the whole journey. Never eats the 2h cap. A short, deliberate interview-DSA band concentrates in Phase 4.

---

## 🐍 Knowledge Unlocked

- Variables, data types, type casting
- Strings (slicing, methods, f-strings)
- Lists, tuples, sets, dictionaries
- Conditionals; loops (for/while/break/continue)
- Functions (def, return, *args, **kwargs, scope, closures)
- Modules (import, from/import, `__name__`, standard library)
- Error handling (try/except, custom exceptions) + File I/O (open/read/write/append, `with`)
- **Testing (Day 11):** pytest basics (`test_*` auto-discovery, plain `assert`), `pytest.raises` for the failure path, import-safety prerequisite (`__main__` guard), reading a failure report as evidence
- **Debugging-from-evidence (Day 11):** reproduced a real bug with a FAILING test FIRST, then fixed it (`Dataset.split` leakage)
- **Data/test concepts (Day 11):** train/test leakage from an unshuffled sorted split; seeded shuffle for reproducibility; *flaky test* = a pass that depends on luck (caught via seed-scan)
- **Reliability spine (started Day 11):** `.gitignore` ✅
- **Error design (Day 12):** *raise, don't swallow* — printing/returning `None` on error hides failures and lies to the caller; **"raise low, catch high"** (small helpers report; the boundary — API/CLI — handles). Deleted dead catch-and-reraise in `safe_divide`/`safe_int`.
- **Property-based testing (Day 12):** Hypothesis (`@given` + strategies, e.g. `st.lists(st.integers())`) — assert a *law* true for ALL inputs, not hand-picked examples; **shrinking** boils a failure down to its minimal repro (caught a deliberate `split` bug, shrank to `[0]`). Multiset compare via `sorted(a) == sorted(b)`.
- **Tooling/debugging (Day 12):** PyCharm was running pytest tests with the **unittest** runner → fixed (Default test runner = pytest + delete stale run config). A reproduce→hypothesize→fix tooling rep.
- **NumPy first-contact (Day 15):** an `ndarray` = a vector / list of numbers you operate on **all at once**; **vectorization** = one whole-array op instead of a Python loop (element-wise `+`, `*`, and **broadcasting** a scalar against every element). `np.maximum(0, arr)` = ReLU over a whole layer (the *real* activation, vs the Day-4 scalar `max(0, x)`); contrast `np.maximum` (element-wise) vs `np.max` (reduces to one value). Measured the payoff — Python loop **167×** slower than the vectorized call via a `time.perf_counter()` sandwich, and learned **a timestamp is absolute — subtract start/end for elapsed, never divide**. **Tooling:** `uv` (≈ Flutter `pub`): `uv init --bare` → `uv add numpy` → committed `pyproject.toml` + `uv.lock`; pointed PyCharm's interpreter at the uv `.venv`.
- **Testing as design (Day 13):** `@pytest.mark.parametrize` — feed a *table* of input rows; one test body runs once per row and each row is its **own named test** (`test_divide[4-2-2.0]`), so a failure points at the exact input (self-locating). Design rule **one test = one question** — happy-path return-checks and a `pytest.raises` failure-path check live in *separate* tests, not crammed into one. **Fixtures** = dependency injection for tests (≈ Flutter `get_it`/`Provider`): a `@pytest.fixture` *builds* the object and the test **requests it by parameter name**; pytest injects it; default function scope = a fresh instance per test. The tell of a real fixture: setup (the data) moves INTO the fixture and the test body shrinks to pure intent.
- **Reductions & the loss function (Day 16):** a **reduction** = whole-array IN, **one number OUT** (the opposite of element-wise) — `arr.mean()` / `arr.sum()` collapse an array to a scalar. Built **MSE** (Mean Squared Error) end-to-end vectorized, no loop: `((predictions - targets) ** 2).mean()` — **square** does two jobs: kills the sign (so +/− errors can't cancel to a fake "0 error") AND punishes big misses disproportionately (off-by-10 = 100 counts 4× an off-by-5 = 25); **mean** summarizes over all points → one "how wrong am I" number (19.75). Syntax-gap fix: a NumPy op already returns an `ndarray` — don't re-wrap in `np.array()`. **Gradient-descent intuition (3B1B ch.2):** loss is a landscape over the weight `w`; the **gradient** `dL/dw` = the slope (of the tangent line) under your feet; to cut the loss, step `w` **opposite** the slope by a small **learning rate** (`w = w − lr × dL/dw`), repeat — the blindfolded hiker walking downhill. Caught the **local-vs-global minimum** nuance. *Still fuzzy → reinforce Day 17:* the update step itself (step opposite, by lr, repeat).
- **Gradient descent, hand-built (Day 17):** the prediction is now a *function of the weight* (`pred = w·x`), so **learning = searching for the `w` that minimizes the loss**. **Numerical (finite-difference) gradient:** slope = **rise ÷ run** = `(loss(w+ε) − loss(w)) / ε`. **ε (epsilon)** = a *tiny nudge you choose* to probe the ground — NOT a fixed "smallest unit" (you can always go smaller); you **divide by ε** to convert "how much the loss fell" into a **rate** ("how *steeply* it falls", independent of how big the nudge was — same idea as speed = distance ÷ time); as ε→0 this rise÷run *is* the derivative `dL/dw`. **The update step (was fuzzy → now solid):** `w = w − learning_rate · slope`; minus × a *negative* slope = a step *toward* the valley = "opposite the slope". **learning_rate** = the step-size knob (too big overshoots/oscillates, too small crawls; the exact `1/curvature` would land in ONE step = Newton's method). **Convergence behaviour:** near the minimum the slope → 0, so steps **auto-shrink (self-brake)**; `w` approaches the true weight **asymptotically, never exactly** (the gap shrinks by a constant factor each step, Zeno-style — here `gap = 2·0.85ⁿ`) — and that's *fine* (loss becomes negligible), which is exactly why tests assert `abs(w−2) < tol`, **never** `== 2`; on noisy real data an exact "true weight" may not even exist (the best `w` still leaves error). **The payoff:** this five-move loop, scaled to billions of weights with autograd instead of finite differences, is *literally* how every modern model (Opus, Gemini, …) is trained.
- **Analytic gradient via the chain rule (Day 18):** swapped the finite-difference *probe* for the *exact* derivative computed by hand. **The chain rule as "multiply the per-step ripple factors":** a tiny nudge to `w` ripples forward through each line of the loss, and each step multiplies the ripple by its *rate* — `pred = w*x` → `×x`, `pred − target` → `×1`, `error²` → `×(2·error)` (the **power rule** / square-strips: grow a square's side, its area grows by two strips → `2·side`, so the exponent 2 drops down). Multiply them: **`dL/dw = mean(2·x·errors)`**, reusing the same `errors = pred − target` from the loss. Verified analytic *equals* finite-difference (both **−30** at w=0; they differ only by the forward-ε bias ~7.5e-4). **A multiplier is a *rate* (out-wiggle per in-wiggle), NOT the line's output value** — the slip that printed `0.0` was using `pred` (the output, =0 at w=0) where the rate is `x`. **The update step needs only the gradient, not the loss value** (`w = w − lr·grad`): the loss is the *scoreboard* (watch it fall / decide when to stop), the gradient is the *steering wheel* — which is precisely why `loss()` was deletable on Day 18 but essential on Day 17 (whose slope was *built from* loss calls). **Testing-as-design carryover:** a loose range assert (`-30 <= grad(0) <= 0.01`) passes even for a wrong −10 → tightened to a tolerance tripwire (`abs(grad(0) − (−30)) < 0.01`), the same "within tol, never `==`" shape as the convergence test. This hand-derived chain rule, run through many layers by autograd, *is* backprop.
- **Building with an LLM API — first interactive chatbot (Day 24):** turned a one-shot Gemini call into a **multi-turn chatbot** — a `while` loop reading `input()`, sending each turn, printing the reply — with **memory** via the Interactions API (`client.interactions.create(..., previous_interaction_id=prev_id)` chains turns server-side; store `interaction.id` each turn, feed it into the next). **Three real production lessons, learned by hitting the errors live:** (1) **free-tier quota is per-PROJECT, not per-API-key** — making new keys doesn't reset a 429 (quota is tied to the Google-Cloud project); RPD resets midnight US-Pacific. (2) **Model selection is a cost/limit decision** — the newest premium model (`gemini-3.5-flash`) has a stingy free cap; a `-flash-lite` model (`gemini-3.1-flash-lite`, 15 RPM / 1000 RPD) is the right tool for building/testing — save the premium model for when quality matters. (3) **Model IDs churn** — a 404 "no longer available to new users" means check the live models page and swap the string. **Two fundamentals cemented by self-inflicted bugs:** **(a) a change to a local variable dies at `return`** — moving `prev_id` from a `global` to a function parameter silently broke memory because the function only updated its *local copy*; the fix is to **return the new value and have the caller store it** (functions report back via `return`, not by mutating their params). **(b) every `return` path must share one shape** — success returned a 2-tuple but the `except` returned a bare string, so the caller's `a, b = aiBot(...)` threw `ValueError: too many values to unpack` on the first 429 (proven by a runnable repro); the fix returns `(msg, prev_id)`, which also preserves the conversation id through a transient error. Carryover of Day-12 *"raise, don't swallow"*: keep the friendly catch at the boundary, but `print(e)` so real bugs still surface to the developer.
- **Learning-rate landscape & tests-as-tripwires (Day 22, consolidation):** the **learning rate** sets the stride length down the loss valley, and the *whole* convergence behaviour pivots on it — watched all three regimes on the live `w`: **too small** (0.01) = baby steps, `w` crawls up to 2 **from one side and never crosses it**; **just right** (0.1) = lands on 2 to ~13 decimals with tiny *inward* bounces; **too big** (2.0) = strides **overshoot the minimum and bounce *outward*** — the gap grows each step (sign flips AND magnitude explodes: `~1e70 → 1e73` in three steps → `nan`), i.e. **divergence**. The boundary: a perfect step (`1/curvature`) lands in one move (Newton, flagged Day 17); below it = one-sided creep, above it = overshoot-inward, well above = explode. **Tests-as-tripwires (carryover from Day 12–13):** the Day-18 assert `abs(w−2)<0.01` **correctly failed** on the diverged run — a test's job is to refuse to certify a broken result; one that stayed silent while training blew up would be *lying*. So an `AssertionError` there = the safety net working, not the code breaking. **Meta-lesson (process):** the cure for "don't feel like it" is to shrink the ask until *starting* is trivial ("just open the file and hit run") — momentum, not willpower; then curiosity ("wait, why did it overshoot?") pulls the real learning.
- **Building a web UI for an LLM app — Gradio + per-session state (Day 25):** `gr.ChatInterface(fn=...)` turns a `fn(message, history)` into a full browser chat (input, thread, retry/clear) with one `.launch()` (serves `http://127.0.0.1:7860`, blocks until Ctrl+C); `history` is the **messages format** (list of `{"role","content"}` dicts) — the old `[(user,bot)]` tuple format was **removed in Gradio 6**. **The core concept — a component passes its VALUE, not itself:** exactly like the built-in textbox hands your `message` param the *string* typed (not the Textbox object), a component in `additional_inputs` hands your function the *value inside it*. So a `gr.State(None)` (an invisible per-session "box") wired into `additional_inputs` arrives at the `prev_id` param as its *contents* (`None`, then the id), and listing the **same** State in `additional_outputs` writes your returned id back into the box for next turn — the round-trip that gives each browser session its own memory. **Why not a global:** one Gradio process serves many sessions off one module, so a module-level `prev_id` is a single slot every user stomps on → cross-session memory leak; per-session state must live in `gr.State`. **Day-24 lesson, framework-enforced:** first cut reassigned a dead local and returned only the reply → the new id was lost → fixed by *returning* `(reply, new_id)` so the caller (Gradio's session store) holds it — the "report back via return, don't mutate-and-hope" move again. **The gotcha:** a State in `additional_inputs` but **not** `additional_outputs` never updates (frozen at its init value) — it must be in **both**. **Deploy-readiness noted:** a Hugging Face Space needs a self-contained `app.py` (inline `aiBot`, not a cross-file import) + `requirements.txt` + README `sdk: gradio` front-matter + the API key as a Space Secret (`GEMINI_API_KEY`).
- **Deploying an LLM app to a public URL — tunnel vs. host (Day 27):** took the local Day-25 Gradio app live. **Tunnel vs. host:** `demo.launch(share=True)` opens a **tunnel** — a tiny `frpc` helper on his laptop dials *out* to Gradio's public relay (`*.gradio.live`), which forwards visitors back down that open pipe to his still-running local server; kill the process and the link dies, and every visitor uses *his* machine + API key. A real **host** (Render) instead *runs his code on their computer* — no laptop dependency, survives closing the lid. **`0.0.0.0` means two different things:** as a server *bind* address (`server_name`) it's "listen on ALL interfaces" — required so the host's front-door proxy can reach the app (bind `127.0.0.1` and the proxy is locked out → **502**); as a browser *destination* it's invalid (`ERR_ADDRESS_INVALID` → browse to `localhost` instead). **Port injection:** the platform picks the port and hands it to the app via the **`PORT` env var**; read it with `int(os.environ.get("PORT", 7860))` — cast to `int` because env vars are always **strings** (the classic "works locally, breaks in the cloud" trap, since the `7860` local fallback is already an int), default `7860` so the same file runs both places. **Secrets as env vars:** the API key never enters the repo — `genai.Client()` reads `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) from the environment, set as a **Render secret** at runtime (a typo'd name = every message fails, masked by the `except` as "rate limit / error"). **Reproducible builds:** a fresh host builds from `requirements.txt` alone — **pin `==`** to the exact tested versions so "works on my machine" transfers. **Self-contained deploy unit:** `app.py` must carry its own code (inlined `aiBot`, dropped the cross-file import — the #1 deploy blocker, a ModuleNotFoundError) in an isolated folder (Render **root directory**) so the build ignores the rest of the repo. **Ops reality:** HF paywalled Gradio Spaces mid-flight → adapted to Render (the roadmap's documented fallback); Render auto-guessed a `uv sync` build (caught + swapped to `pip install -r requirements.txt`); free tiers **cold-start** (~30–60s) after ~15-min idle.
- **Streaming an LLM reply live — generators as a stream (Day 28):** a function that `return`s is one-shot (a Dart `Future`); a function that `yield`s is a **generator** = a stream of values over time (a Dart `Stream`/`async*`). **Gradio's contract:** if `fn` is a generator, `ChatInterface` *iterates* it and **repaints the chat bubble on every `yield`** — so "streaming" isn't a Gradio toggle, it's an emergent property of handing Gradio something iterable. **`yield` the whole growing string (`acc`), not the new fragment** — Gradio *replaces* the bubble each yield (doesn't append), so yielding only the delta would flicker one letter at a time. **The Gemini half:** `client.interactions.create(..., stream=True)` returns an **event stream**, not a response object — there is **no `.output_text`**; you accumulate `event.delta.text` yourself, guarded by `event.event_type == "step.delta"` **and** `event.delta.type == "text"` (other event types — `step.start/stop`, `interaction.completed` — carry no text and fall through). The **new interaction id arrives on the FIRST event** (`interaction.created` → `event.interaction.id`), *before* any text, so you carry it in every yielded `(acc, new_id)` tuple and `gr.State` stays correct mid-stream. **Streaming and memory are independent** — adding `stream=True` didn't touch the `previous_interaction_id` chain. **Two self-found bugs (debugging-from-evidence):** (1) a wrong event-type string (`"interaction"` vs `"step.delta"`) meant the accumulate branch never fired → a **blank bubble** was the evidence that pinned it; (2) **`return` inside a generator does NOT hand the value back** — it raises `StopIteration` and the value vanishes, so the friendly error must be **`yield`ed, not `return`ed** (Day-24's "every path shares one shape" lesson, generator edition). This `yield`-as-you-go pattern is exactly the server-side **SSE token streaming** flagged for Phase 3, and pre-wires a Flutter `Stream` client.
- **Branches, PRs & writing for the next reader (Day 29):** **A branch is a lightweight movable pointer to a commit — not a copy of your files** (which is why creating one is instant). `main` is what Render deploys, so working on a branch is the first time his change could exist *while production stayed safe*. **A PR is not paperwork — the diff view IS the review**: the last cheap moment to catch a stray edit before it's public (he read his: one function replaced, `aiBot` gone, launch line untouched — exactly the intended change and nothing else). **Squash vs. merge commit (learned the hard way):** he hit the default button → `main` now carries a **2-parent merge bubble** *and* both original commits, including the bad "Created a branch…" message; a **squash** would have collapsed them into ONE clean commit carrying only the PR title. Left in place deliberately — **rewriting pushed history is worse than an ugly history**. **The PR description is the trophy, not the branching:** *the diff tells the reader WHAT changed; the description tells them what they can't see — WHY it was worth changing, and WHAT PROOF exists that it works.* Hence What / Why / **How I tested** (the last has no official GitHub guidance — it's professional convention, and it's the line that makes a reviewer trust the diff instead of re-deriving it). **The title test: "If merged, this PR will ___."** If it doesn't complete that sentence, it's narrating your afternoon, not describing a change ("Created a branch streaming-deploy" fails; the reader is *standing on* the branch). **Hedges carry zero information** — *"change the mechanics of how X works"* is what every commit does by definition; engineers write the falsifiable claim (*X now does Y*), because unreviewable writing is how bugs get merged. And it's not cosmetic: **on a squash merge the PR title becomes the commit subject on `main` forever** — it's the line future-him greps. **Scope discipline:** the identical buggy `print` in `day28.py` was left untouched — it only ever runs on a TTY where there's no bug, and an unrelated file in a PR titled "streaming deploy" makes a reviewer reason about one more thing. **Precision when describing bugs:** "fixed the print to *allow Render to show the logs*" is backwards — Render never stopped showing logs; **Python wasn't sending them**. Name the actor that actually misbehaved.
- **stdout buffering: the third "works locally, breaks in the cloud" trap (Day 29):** Python **inspects where stdout is going and silently changes strategy**. To a **TTY** (his laptop terminal) it **line-buffers** — every `print` appears instantly. To a **pipe** (Render, Docker, CI, anything capturing output) it **block-buffers into a ~128KB tray** and only sends when the tray fills. A low-traffic chatbot never fills 128KB, so his `print("(debug)", e)` sat unsent — and after ~15 min idle Render spins the free instance down, the process dies, and **the tray is discarded unread**. The trap's teeth: **uvicorn logs to *stderr*, which is unbuffered**, so the Render log tail looks perfectly healthy while his diagnostics are silently missing → he'd have concluded "no exception ever fired." **Two fixes, a real trade-off:** `flush=True` on the call (**explicit, lives in the repo, travels to any host** — but fixes only that one print) vs. **`PYTHONUNBUFFERED=1`** as a host env var (**fixes every print at once, no code change** — but lives in a dashboard, not the project, so a clone deployed elsewhere silently regains the bug = *"works on my Render"*, the same disease as "works on my machine"). He chose `flush=True`; real production containers usually set the env var too, once there are hundreds of prints. **Found by reading the signature:** `print` has four keyword params he'd never used — *a parameter you didn't know existed is the #1 reason people conclude "Python can't do this."* **Compounding weakness noted:** a bare `except Exception` collapsing 429s / stale interaction ids / auth errors into one identical friendly string leaves zero signal to tell them apart — the buffering just hid the only clue. (Mitigation now available: **Interactions API logs are visible in AI Studio** as of ~Jul 2026.) **Empirically settled (undocumented anywhere):** Render's proxy does **NOT** buffer Gradio's SSE stream — streaming survives the host proxy intact. **Skeptic-verified:** `gr.State` is genuinely per-session under real concurrency — many visitors on one Render instance do **not** leak conversations into each other (the Day-25 "never use a module-level global" instinct, holding up under the exposure it was designed for). **Parked (latent, pre-existing, not port-introduced):** if Gemini ever returns **zero text deltas** (e.g. a safety-blocked reply), the generator yields nothing and Gradio raises `RuntimeError: async generator raised StopAsyncIteration` → a red error toast instead of his friendly message; his own `except` can't catch it because the failure happens in Gradio's wrapper *above* his frame. Likelier in production than locally — **a public URL takes random input from strangers**.

---

## 🗺️ Phase Roadmap (v2 — true ~16-month critical path)

| Phase | ~Duration @2h/day | Focus | Deployed milestone |
|-------|-------------------|-------|--------------------|
| **1 — Python delta + reliability spine + math-with-code + data** | ~15–16 wks (in progress; refine, don't restart) | Pythonic gaps, harden own code, NumPy/pandas, messy data | NumPy logistic-reg → clean a real CSV → **Gradio app on a public URL (Render — HF paywalled Gradio Spaces Jul 2026)** ✅ deploy done Day 27 |
| **2A — Classical ML + Evaluation + FastAPI ladder → `/predict`** | ~18–20 wks | Weakest+most-wanted area. Train a model FIRST, then climb FastAPI one rung at a time, then interlock | **Dockerized FastAPI `/predict`** (API+Postgres), CI tests, deployed, latency p50/p99 **under load** |
| **2B — Deep Learning** | ~5–7 wks · **OPTIONAL** | fast.ai (top-down) + PyTorch. Skippable without blocking Phase 3 | Optional: a NN beating the 2A classical baseline |
| **3 — Transformers intuition + RAG + LLM Evals + Agents → MCP** | ~20–22 wks | LLM/agent track via APIs (no from-scratch GPT needed). Evals = your signature | **Traced RAG-over-docs + eval harness**, then an **agent with failure-recovery + prompt-injection defense** |
| **4 — Production/MLOps + Portfolio + Job hunt (concurrent)** | ~16–18 wks | Prove "elite & reliable in deployments." Apply *while* finishing | **Monitored full-stack flagship** (MLOps Zoomcamp project = the flagship), CD, SLO+runbook |

> **Buffer week every ~6 weeks:** re-deploy an old project cleanly, refactor, redo Anki. No new concepts. Counts for streak. Pops 🥈 Craftsman. (Burnout valve.)

---

### Phase detail

> ⬇️ **PLANNING ARCHIVE — do not read this daily.** Your daily view is the Status block at the top (Today + next trophy + weekly sub-goal + freeze tokens). Everything below is for planning only.

**Phase 1 — Python delta + reliability spine + math-with-code + data**
- Pythonic delta: generators (≈Dart Stream), decorators, context managers, dunder methods, `asyncio` (≈Dart Future/async — your future FastAPI superpower).
- **Reliability spine, DRIBBLED in (a tax on real work, not a plumbing block):** `.gitignore` ✅ → `uv` + `pyproject.toml` when NumPy is first needed → `pytest` the first time a function has a bug worth a regression test → branches + PR-to-self/squash → `pre-commit` + Ruff LAST.
- **Harden-your-own-code (Day 11):** make `day4.py` run (LinearLayer crash), add a seeded shuffle to `Dataset.split` + a Hypothesis test proving order-independence, move import-time code under `__main__`, make `safe_divide` raise-or-sentinel instead of print-and-None.
- Testing as design: arrange-act-assert, `@pytest.mark.parametrize` (5 inputs not 1), fixtures, `pytest.raises` for the failure path, mock an external call, Hypothesis property tests.
- Debugging-from-evidence loop (reproduce → hypothesize → instrument with pdb → fix → regression test FIRST) = standing "bug closed" definition.
- Math-with-code: 3B1B Linear Algebra + Calculus + StatQuest stats → implement each in NumPy the SAME session. No proofs, no pure-math days.
- NumPy (broadcasting, vectorize) → pandas (messy CSVs, missing values, merge/groupby, leak-free split).
- _Free resources:_ Official Python Tutorial, Google's Python Class, CS50P (free cert), 3Blue1Brown, StatQuest, Kaggle Pandas + Data Cleaning micro-courses, pytest/Hypothesis/uv/pre-commit docs, Pro Git, Gradio + HF Spaces docs.

**Phase 2A — Classical ML + Evaluation + FastAPI ladder**
- Classical ML: from-scratch THEN sklearn for linear reg, logistic reg, one decision tree; k-NN + ensembles sklearn-first/concept-only.
- Evaluation first-class: when accuracy lies (imbalance), precision/recall/F1, ROC-AUC vs PR-AUC, cross-validation, DATA LEAKAGE, MAE/RMSE/R². **New rule: justify the metric, don't just beat the baseline.**
- Experiment tracking: W&B free tier, seed everything, log git SHA + data hash + config, one-command reproduce.
- **FastAPI reliability ladder (ONE rung at a time, +50% first-infra buffer):** HTTP/REST → FastAPI core + auto-docs → Pydantic v2 (≈freezed/json_serializable) → DI + async (`Depends`, never block the loop) → raw SQL (JOINs/indexes/N+1) → PostgreSQL → SQLAlchemy 2.0 sync THEN async → Alembic (up+down) → Auth (OAuth2+JWT, Argon2) → error design (RFC 9457).
- Async failure-modes day: pool exhaustion, blocking the loop (`run_in_executor`), graceful shutdown, timeouts/cancellation, backpressure — paired with a load test (locust/hey) so latency is p50/p99 under concurrency.
- One-page DESIGN DOC before each milestone; pytest interleaved (async tests via `httpx.AsyncClient`; SQLite/throwaway Postgres for tests — Testcontainers deferred to Phase 4).
- _Free resources:_ StatQuest, Andrew Ng ML (videos only — labs/cert paywalled), scikit-learn docs, FastAPI + SQLAlchemy 2.0 docs, W&B free tier, locust/Pandera docs.

**Phase 2B — Deep Learning (OPTIONAL, trophy-gated)**
- fast.ai top-down (budget debugging time, notebooks break against current libs) → PyTorch (Daniel Bourke; skip TensorFlow).
- OPTIONAL deep dive: Karpathy "Zero to Hero" micrograd → makemore (gated behind a trophy, never a blocker).

**Phase 3 — Transformers intuition + RAG + Evals + Agents → MCP**
- Transformer INTUITION only on the critical path (3B1B attention + HF LLM Course concepts). From-scratch GPT = optional enrichment.
- Prompting → RAG → Fine-tuning IN THAT ORDER. Prompts are code — version them in Git.
- RAG: chunking → embeddings (free local BGE/sentence-transformers) → **pgvector** (reuse your Postgres; Qdrant only if >~1–5M vectors) → hybrid search + reranking → generation. Retrieval/chunking quality > the DB.
- Fine-tuning: LoRA/QLoRA CONCEPTUALLY; the actual fine-tune is optional enrichment. RAG/prompting/tools solve ~95% of problems.
- **LLM EVALS (first-class, your signature):** Hamel Husain's evals guide + LLM-as-Judge; cheap code checks first, binary pass/fail, golden set ≥20 Q&A; Langfuse tracing from the first call; promptfoo gating in CI. Two tools only (Langfuse + promptfoo).
- Testing non-deterministic code: assert on schema not exact text, temp=0 seeding, snapshot tests.
- Agents: plain tool-calling loop first, feel the limits, THEN HF Agents Course + MCP (modelcontextprotocol.io). LiteLLM fallback + per-call cost logging.
- **Security:** OWASP LLM Top-10; fold prompt-injection cases INTO the eval golden set (baseline: agent resists N injections).
- SSE token streaming server-side (`StreamingResponse` + cancel cleanup) — your Dart Stream knowledge, server-side; pre-wires a Flutter client.
- _Free resources:_ HF LLM + Agents Courses, Hamel Husain evals blog, Langfuse free tier, promptfoo, pgvector/sentence-transformers/LiteLLM docs, OWASP Top-10 for LLMs PDF.

**Phase 4 — Production/MLOps + Portfolio + Job hunt (concurrent)**
- **MLOps Zoomcamp (DataTalks.Club, free cert via ONE end-to-end project that IS the flagship):** Docker deepening, MLflow, orchestration, batch/real-time deploy, monitoring (Evidently/Prometheus, drift).
- Reliability hardening: circuit breakers, idempotency keys, slowapi rate-limiting, PII redaction before logs, per-trace cost, **Redis pulled in here** (LLM response caching / job queue via ARQ), **Sentry** error monitoring + **Testcontainers** (both deferred to here, not earlier), full CD on merge.
- Operational mindset: ONE SLO per service, ONE alert + ONE runbook; Black-Box-Recovery on-call drill; postmortem artifact.
- Serving VOCABULARY only (1 day): vLLM / Ray Serve / BentoML — read 3 posts, 5 sentences each (résumé keywords, not buildable in budget).
- Interview prep CONCURRENT: ML/AI system design priority; DSA simmer (Blind 75 to clear filters); rehearse the eval answer + "when NOT to use an LLM."
- Portfolio: 3–4 deep deployed reproducible projects (RAG-over-docs, agent-with-recovery, classic-ML service), each with a design doc, README-as-narrative, cost+latency numbers, honest limitations, teardown post. NOT 15 notebooks.
- _Free resources:_ MLOps Zoomcamp (+free cert), Made With ML, Evidently/Prometheus/slowapi/ARQ/Redis docs, NeetCode free tier, "Designing ML Systems" via free talks.

---

## 🏗️ Tech Stack (pulled in when a measured need appears — NOT on a calendar)

```
Mobile (optional moat): Flutter / Dart            → Phase 4 capstone bonus only
Backend:                FastAPI                    → Phase 2A (after a model exists)
Database:               PostgreSQL + SQLAlchemy 2.0 async + Alembic → Phase 2A
Validation:             Pydantic v2 / Pandera      → Phase 2A
Vector DB:              pgvector (default) → Qdrant only if >~1–5M vectors → Phase 3
Experiment tracking:    Weights & Biases (free)    → Phase 2A
LLM eval/observability: Langfuse + promptfoo (two, not five) → Phase 3
Cache / queue:          Redis + ARQ                → Phase 4 (LLM caching / jobs)
MLOps:                  Docker, GitHub Actions, MLflow, Evidently/Prometheus → woven, deepened Phase 4
Deploy ($0, verified Jul 2026): GitHub → Render free Web Service (bind 0.0.0.0 + $PORT; ~15-min idle spin-down ≈30-60s cold start). ⚠️ Hugging Face PAYWALLED Gradio/Docker Spaces ~Jul 8 2026 (PRO $9/mo; only Static free) — Render is the default $0 host now
  └ Render gotchas learned by shipping: SSE streaming passes through the proxy UNBUFFERED (verified Day 29 — undocumented anywhere else, so trust this line over the internet); but PYTHON block-buffers stdout to a pipe → print() needs flush=True or PYTHONUNBUFFERED=1 or your logs silently vanish. Workspace auto-migrates Aug 1 2026: still free, bandwidth 100GB → 5GB.
GPU (free):             Google Colab / Kaggle (~30 GPU-h/wk; checkpoint for re-runs)
```

---

## 📐 Math & DSA Stance

- **Math:** engineer-focused, just-in-time, code-embedded, **ZERO pure-math days**. Method: 3B1B/StatQuest video → implement in NumPy the same session. Phase-1 target = intuition only (linear algebra, gradients/chain rule, probability basics, descriptive stats). No proofs. Heavier math arrives only when a model demands it (optional Karpathy track).
- **DSA:** interview hygiene only — ~1 NeetCode pattern problem/week toward Blind 75, concentrated band in Phase 4. ~70% of senior AI roles have no LeetCode; reinvest the time in system design + write-ups + evals.

---

## 🦋 Flutter Strategy (optional, decided later — pre-wired as the moat)

Every phase is engineered so Flutter plugs in with **zero rework**, gated behind the highest trophy (always a bonus, never a dependency):
- **Phase 2A:** design the `/predict` JSON contract (in the milestone's design doc) so a Flutter client *could* consume it — don't build the client.
- **Phase 3:** implement SSE token streaming server-side — your Dart `Stream<T>` knowledge applied server-side; a Flutter `Stream` plugs straight in.
- **Phase 4 (the slot):** polished Flutter app → streaming FastAPI → RAG/agent + classic-ML, with latency + cost + evals dashboards. Un-fakeable by notebook-only candidates. Earns 🏆 Full-Stack AI (SSS). If time slips, it's dropped before any hireable core — costs nothing, since the API contract + streaming were built for their own sake anyway.

---

## 📦 XP Log

| Event | XP Change | Running Total |
|-------|-----------|---------------|
| Days 1–8 completed | +270 | 270 |
| Day 9 skipped | −25 | 245 |
| Day 10 completed (coding day) | +35 | 280 |
| Day 11 completed (hardening + first tests; 🥉 Green Check + 🥈 Red-Green) | +40 | 320 |
| Day 12 completed (finish hardening + first property-based test; 🥉 Property Prover) | +40 | 360 |
| Day 13 completed (testing as design: parametrize + first fixture; no new trophy) | +30 | 390 |
| Day 14 — true rest day (new Sunday policy; not a skip, no penalty) | +0 | 390 |
| Day 15 completed (NumPy first-contact: vectorized ReLU 167× over a loop + first uv lockfile; 🥉 Vectorized + 🥉 Clean Tree) | +40 | 430 |
| Day 16 completed (NumPy reductions → vectorized MSE loss + gradient-descent intuition; no new trophy) | +30 | 460 |
| Day 17 completed (hand-rolled single-weight gradient descent: finite-difference slope + `w = w − lr·slope`, 50-iter convergence to w≈2 / loss→~0; 🥉 Gradient) | +40 | 500 |
| Day 18 completed (analytic gradient via chain rule: `grad = mean(2·x·errors)` replaces finite-diff slope, two green asserts incl. a tightened tolerance tripwire; analytic-gradient micro-pop, no new trophy) | +30 | 530 |
| Day 19 frozen (Streak-Freeze token spent — miss absorbed, streak preserved, no penalty) | +0 | 530 |
| Day 20 frozen (second Streak-Freeze token spent — absorbed) | +0 | 530 |
| Day 21 — Sunday true rest day (streak-neutral) | +0 | 530 |
| Day 22 completed (re-entry after gap: re-ran Day-18 green + mapped the full learning-rate landscape experimentally — crawl/land/diverge — and saw the tolerance assert catch a diverged run; consolidation, no new artifact) | +15 | 545 |
| Day 23 completed (re-entry + PIVOT to build-first; shipped first working LLM API call from Python via Gemini free tier — 🥉 First Token, a Phase-3 trophy pulled ~8 months forward) | +40 | 585 |
| Day 24 completed (first interactive chatbot: multi-turn CLI loop with memory + graceful 429 handling; 3 production lessons — per-project quota, model-selection, model-ID churn — + 2 fundamentals-fixing bugs; shipped working code, no new trophy) | +35 | 620 |
| Day 25 completed (first browser chatbot: Gradio `ChatInterface` wrapping the Day-24 bot + per-session memory via `gr.State` through `additional_inputs`/`additional_outputs`; new tool Gradio 6.20; concept "a component passes its value not itself" + Day-24 return-don't-global reinforced; shipped a working local web app, no new trophy — First Deploy pops Day 27) | +35 | 655 |
| Day 26 — Sunday true rest day (streak-neutral) | +0 | 655 |
| Day 27 completed (🥉 **First Deploy**: deployed the Gradio chatbot to a public Render URL, memory verified in the cloud; navigated the HF Gradio paywall → Render pivot; self-contained `app.py` w/ `0.0.0.0`+`$PORT` binding + pinned `requirements.txt`) | +45 | 700 |
| Day 28 completed (streaming chatbot: `random_response` → generator with `interactions.create(stream=True)`, accumulate `step.delta` + `yield` the growing string; per-session `gr.State` memory kept; two self-found bugs fixed — wrong event name + `return`-in-a-generator; verified types live + remembers; commit `b7cb99c`; no new trophy — a skill/feature day) | +35 | 735 |
| Day 29 completed (🥉 **PR Author**: first branch → PR-to-self #1 → merge, shipping Day-28's streaming to production and **verified live at the public URL**; caught + fixed a cloud-only stdout block-buffering bug that made Render's logs lie; settled an undocumented question empirically — Render does not buffer Gradio SSE; skeptic-verified per-session `gr.State` under concurrency. Docked nothing for the two honest misses (merge-commit instead of squash; PR body still missing Why/How-tested) — they're logged as PR #2's bar) | +40 | 775 |
| **Current Total** | | **775** |

> **New XP philosophy (v2):** DONE = shipped + tested + deployed + baseline-beaten *out-earns* watching courses. Finishing a tutorial pays little; shipping a deployed, tested, baseline-beating artifact pays a lot. (Past XP is left as-is — no retroactive churn.)

---

## 🏆 Rank Progression

```
E → D → C → B → A → S → SS → SSS
↑
HERE
```

---

## 🏆 Trophies / Achievements (v2 ladder)

> Permanent once popped. Already-earned trophies carry over untouched. 🥉 Bronze · 🥈 Silver · 🥇 Gold · 🏆 PLATINUM = elite AI engineer + the job.
> **Retired:** ~~🥉 Mathematician~~ (pure-math days removed).

**Earned so far: 18**

### Phase 1 — Python · reliability spine · data
- [x] 🥉 **Hello, Python** — Day 1
- [x] 🥉 **Data Wrangler** — mini tokenizer (Day 2)
- [x] 🥉 **The Optimizer** — first LeetCode (Two Sum, Day 3)
- [x] 🥉 **Class President** — first OOP classes (Day 4)
- [x] 🥉 **Wordsmith** — Week 1 Text Analyzer (Day 6)
- [x] 🥉 **Modular** — first reusable module (Day 8)
- [x] 🥉 **Graceful Under Pressure** — first custom exception (Day 10)
- [x] 🥉 **Persistent** — read & write your first file (Day 10)
- [x] 🥉 **Clean Tree** — `.gitignore` ✅ + green `uv` lockfile ✅ (`pyproject.toml` + `uv.lock`, numpy 2.4.6) — Day 15
- [x] 🥉 **Green Check** — first passing pytest test (on `checked_sqrt`) — Day 11
- [x] 🥈 **Red-Green** — failing test reproduced `Dataset.split` leakage, then fixed it (seeded shuffle) — Day 11
- [x] 🥉 **Property Prover** — first Hypothesis property-based test (`test_split_conserves` — a conservation law over `Dataset.split`, verified by watching it shrink a planted bug to `[0]`) — Day 12
- [ ] 🥉/🥈 **Bug Bounty** *(repeatable)* — a bug closed only after a regression test reproduces it first
- [ ] 🥉/🥈 **Baseline Beaten** *(repeatable)* — each time a project beats its documented numeric baseline
- [x] 🥉 **Vectorized** — `np.maximum(0, c)` replaced a Python ReLU loop, **167× faster** (documented baseline) — Day 15
- [x] 🥉 **Gradient** — hand-rolled single-weight gradient descent: finite-difference slope + `w = w − lr·slope`; a 50-iter loop converged `w → ~2`, loss `30.0 → ~0`, slope self-flattened to 0 (resource: 3B1B ch.2 + StatQuest GD step-by-step) — Day 17
- [ ] 🥉 **First Model** — NumPy logistic regression beats the majority-class baseline (resource: StatQuest)
- [ ] 🥉 **From Raw** — 3 micro-pops: First Merge/Join · Killed the NaNs · Leak-Free Split
- [x] 🥉 **First Deploy** — first public URL live: Gradio chatbot on a **Render** free Web Service (https://gemini-chatbot-tw9q.onrender.com/), memory verified in the cloud; **HF paywalled Gradio Spaces → pivoted to Render** — Day 27
- [x] 🥉 **PR Author** — first PR-to-self ([#1](https://github.com/vraj129/ai-mastery-log/pull/1), `streaming-deploy` → `main`), shipping live streaming to production and verified at the public URL — Day 29. **Honest asterisk (the bar for PR #2):** he **merge-committed, not squash-merged** (default button), and the body carried **What but no Why / How-tested**. Awarded on the spirit — he authored, reviewed his own diff, and merged a real feature to a live URL — but the letter of this trophy is unfinished. *PR #2 must be squash-merged with all three lines.*

### Phase 2A — Classical ML · Evaluation · FastAPI
- [ ] 🥉 **Auto-Docs** — first FastAPI `/docs` renders live
- [ ] 🥉 **Typed In** — first Pydantic v2 model rejects a bad payload
- [ ] 🥉 **DI'd** — first `Depends()` dependency wired
- [ ] 🥉 **No N+1** — spotted and killed an N+1 in a query log
- [ ] 🥈 **Metric Defender** — beat a baseline AND justify the metric choice in the README
- [ ] 🥈 **Tracked** — first seeded, reproducible W&B run (git SHA + data hash logged)
- [ ] 🥈 **Time Traveler** — Alembic migration up+down with zero data loss
- [ ] 🥈 **Event Loop Whisperer** — explain in 3 sentences why `time.sleep` stalls an async route
- [ ] 🥈 **Held the Line** — service stays green under a documented concurrent load test
- [ ] 🥈 **Architect** — a one-page design doc that correctly predicted a failure mode you hit
- [ ] 🥈 **Locksmith** — first dependency CVE found + patched (pip-audit/Dependabot)
- [ ] 🥈 **It's Live (Backend)** — model served via FastAPI `/predict`, Dockerized, deployed, CI green

### Phase 2B — Deep Learning (optional)
- [ ] 🥈 **Neuron** — a small NN beats the Phase-2A classical baseline (optional)
- [ ] 🥈 **Backprop Boss** — implement backprop from scratch (optional enrichment)

### Phase 3 — LLMs · RAG · Evals · Agents · MCP
- [x] 🥉 **First Token** — first successful LLM API call (Python via Google AI Studio free tier, `google-genai` + `gemini-3.5-flash`; an AI answered his own code) — Day 23, pulled ~8 months forward by the build-first pivot
- [ ] 🥉 **Chunked** — first document split + embedded into pgvector
- [ ] 🥇 **Observable Agent** — Langfuse trace on the first LLM call
- [ ] 🥇 **Eval Architect** — golden set ≥20 Q&A (counter 0/20→20) + passing eval harness ("the boss-fight detector")
- [ ] 🥇 **Caught a Regression** — your eval harness fails a bad prompt change
- [ ] 🥇 **Beat No-RAG** — RAG beats a no-retrieval answer on the eval set
- [ ] 🥇 **Kill Switch** — agent with failure recovery + a working kill switch
- [ ] 🥇 **Injection-Proof** — agent resists planted prompt-injections (counter 0/N)
- [ ] 🥇 **Cost Aware** — documented cost-per-query + a logged optimization
- [ ] 🥇 **Merged Upstream** — first PR merged into someone else's repo

### Phase 4 — Production · MLOps · Portfolio · Job
- [ ] 🥇 **Halved It** — documented 2× latency-or-cost win with before/after profiles
- [ ] 🥇 **Black Box Recovery** — root-cause a planted bug from logs+traces, with a postmortem
- [ ] 🥇 **Ship It (CD)** — public URL, `/docs` live, CI runs migrations+tests+deploy on push
- [ ] 🥇 **Teardown** — a project-teardown blog post per flagship (folds into the Sunday post)
- [ ] 🏆 **Full-Stack AI (SSS)** — optional Flutter client → streaming FastAPI → RAG/agent + ML, monitored
- [ ] 🏆 **PLATINUM — Elite AI Engineer** — land the role 🎯

### Consistency (streaks)
- [x] 🥉 **Week Warrior** — first 7-day streak
- [ ] 🥈 **Craftsman** *(repeatable)* — complete a consolidation/buffer week (~every 6 weeks)
- [ ] 🥈 **Locked-In-14 / 28 / …** — streak-milestone pop every 14 days
- [ ] 🥈 **Locked In** — 30-day streak
- [ ] 🥇 **Unstoppable** — 100-day streak

---

## 📌 Key Rules

- **2 hours per day HARD STOP.** (Gentle boundary — no countdown-timer pressure.)
- **Sunday = TRUE rest day — MANDATORY, zero tasks.** No reading, no post, no check-in. Rest is infrastructure for a ~16-month plan, not a deviation; resting on Sunday = following the plan. A planned Sunday rest is NEUTRAL for the streak (never breaks it, never pads it) and costs **no XP** — it is NOT a skip. (Full-time job + Sat learning + daily weekday learning = Sunday must be real rest or the engine seizes.)
- **Skipping a day = −25 XP** (the missed topic folds into the next consolidation/buffer week — the day is NOT re-numbered) — UNLESS you spend a **Streak-Freeze token** (absorbs the miss: XP unaffected, streak preserved, day rolls forward). 2 tokens, refill 1/month. *Tip: a token could have absorbed the Day 9 skip.*
- ~~2 consecutive skips = −100 XP + week restart~~ **(DELETED — quit-trigger, not a motivator.)**
- **Consolidation/buffer week every ~6 weeks** (re-deploy + refactor + Anki, no new concepts; counts for streak; pops 🥈 Craftsman).
- **The DONE law** (see Philosophy): in Git + passing test + deployed + baseline beaten, or it's not done.
- **Every project beats a documented NUMERIC baseline** — and (from Phase 2A) you must **justify the metric**.
- **Debugging-from-evidence** is the standing definition of "bug closed": reproduce → hypothesize → instrument (pdb) → fix → write the regression test FIRST.
- **One-page design doc** before every Phase-2+ milestone.
- **Latency baselines measured UNDER concurrent load** (p50/p99), never single-request.
- **FREE resources only.** Web-search AI news before every day plan.
- **Resource-first:** one pinned free resource per task, named before you start. If no single resource fits a milestone, the milestone is too big — de-bundle it into ≤3-day steps.
- **≤3-day pop cadence:** at least one trophy or micro-pop is reachable every ≤3 days; if a stretch has none, insert a micro-pop.
- **One active thread at a time:** finish a phase's main track end-to-end before opening the next (e.g. all of Phase 2A before any optional Phase 2B deep-learning thread). No alternating weeks.
- **Math:** code-embedded, just-in-time, no pure-math days. **DSA:** ~1 problem/week, interview hygiene only.
- **One new infra tool per milestone**, with a +50% first-time buffer.
- **Park It:** stuck 15 min → write the question, move on. 30-min fallback plan every day.
- **Anki:** 1 card per concept, review on phone — favor *syntax* cards (front = the task in plain words, back = the one-liner he writes himself) to close the syntax-recall gap. **Active recall:** last 5 min of each LEARNING day (Mon–Sat, never Sunday), write 3 things from memory.
- **Learn-in-public post = SHIP-DRIVEN, not weekly.** Write a short post only when you ship something worth it (a trophy/milestone), on a Saturday — never a forced Sunday chore. Target ~1–2/month.

---

## 📁 GitHub

**Repo:** https://github.com/vraj129/ai-mastery-log

---

## 🤖 How to Resume on a New Claude Account

Paste this entire file + the full system prompt into your first message, then say:

> "I am resuming my AI roadmap. All context is above. Start Day 24."
