# 🗺️ AI Mastery Roadmap — State File (v2)

> Last updated: June 4, 2026
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

| Field | Value |
|-------|-------|
| **Current Day** | 12 |
| **Rank** | E |
| **XP** | 320 |
| **Phase** | 1 |
| **Today** | Day 12 — Finish hardening: `safe_divide`/`safe_int` raise-not-print (+ regression tests) + Hypothesis order-independence test for `Dataset.split` |
| **This week's sub-goal** | ✅ DONE — day4 runs, first green pytest (🥉 Green Check), `Dataset.split` leakage caught test-first then fixed (🥈 Red-Green) |
| **Streak** | 2 (Day 10 ✅, Day 11 ✅) |
| **Streak-Freeze tokens** | 2 available (refill 1/month) |
| **Start Date** | May 25, 2026 |
| **Next trophy in sight** | 🥉 Clean Tree (½ — `.gitignore` ✅, uv lockfile pending when NumPy lands) |

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
| Day 12 | Finish hardening: `safe_divide`/`safe_int` raise-not-print (+ regression tests) + Hypothesis order-independence test for `Dataset.split` | 🔄 Next (Fri Jun 5 IST) |

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

---

## 🗺️ Phase Roadmap (v2 — true ~16-month critical path)

| Phase | ~Duration @2h/day | Focus | Deployed milestone |
|-------|-------------------|-------|--------------------|
| **1 — Python delta + reliability spine + math-with-code + data** | ~15–16 wks (in progress; refine, don't restart) | Pythonic gaps, harden own code, NumPy/pandas, messy data | NumPy logistic-reg → clean a real CSV → **Gradio app on a Hugging Face Space** |
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
Deploy ($0, verified mid-2026): GitHub CI → Hugging Face Spaces (always-on demo host) → Render (accept ~15-min idle spin-down)
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
| **Current Total** | | **320** |

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

**Earned so far: 11** ( + 🥉 Clean Tree ½ done)

### Phase 1 — Python · reliability spine · data
- [x] 🥉 **Hello, Python** — Day 1
- [x] 🥉 **Data Wrangler** — mini tokenizer (Day 2)
- [x] 🥉 **The Optimizer** — first LeetCode (Two Sum, Day 3)
- [x] 🥉 **Class President** — first OOP classes (Day 4)
- [x] 🥉 **Wordsmith** — Week 1 Text Analyzer (Day 6)
- [x] 🥉 **Modular** — first reusable module (Day 8)
- [x] 🥉 **Graceful Under Pressure** — first custom exception (Day 10)
- [x] 🥉 **Persistent** — read & write your first file (Day 10)
- [ ] 🥉 **Clean Tree** — `.gitignore` ✅ + green `uv` lockfile ⏳ (½ — lockfile pending)
- [x] 🥉 **Green Check** — first passing pytest test (on `checked_sqrt`) — Day 11
- [x] 🥈 **Red-Green** — failing test reproduced `Dataset.split` leakage, then fixed it (seeded shuffle) — Day 11
- [ ] 🥉/🥈 **Bug Bounty** *(repeatable)* — a bug closed only after a regression test reproduces it first
- [ ] 🥉/🥈 **Baseline Beaten** *(repeatable)* — each time a project beats its documented numeric baseline
- [ ] 🥉 **Vectorized** — first NumPy broadcast replacing a Python loop
- [ ] 🥉 **Gradient** — hand-rolled gradient descent on a single weight (resource: 3B1B)
- [ ] 🥉 **First Model** — NumPy logistic regression beats the majority-class baseline (resource: StatQuest)
- [ ] 🥉 **From Raw** — 3 micro-pops: First Merge/Join · Killed the NaNs · Leak-Free Split
- [ ] 🥉 **First Deploy** — first public URL live (Gradio on a Hugging Face Space)
- [ ] 🥉 **PR Author** — first squash-merged PR-to-self (3-line what/why/how-tested)

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
- [ ] 🥉 **First Token** — first successful LLM API call
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
- **Sunday = off** (reflection, 1 paper, 1 post, Sunday check-in).
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
- **Anki:** 1 card per concept, review on phone. **Active recall:** last 5 min, write 3 things from memory.

---

## 📁 GitHub

**Repo:** https://github.com/vraj129/ai-mastery-log

---

## 🤖 How to Resume on a New Claude Account

Paste this entire file + the full system prompt into your first message, then say:

> "I am resuming my AI roadmap. All context is above. Start Day 12."
