# ORACLE — AI Document Reasoning Engine

> **Expert reasoning. Auditable outputs. Every time.**

ORACLE is a structured reasoning engine that transforms complex company information into professional insurance underwriting briefs — with full transparency into how it thinks, not just what it outputs.

Think of it like a GPS for underwriters: it doesn't just tell you "turn left" — it shows you the map, the traffic data, and the alternate routes it considered. If it's unsure about a road, it says so.

---

## The Problem

A senior underwriter reviews a 50+ page commercial submission and produces a 2-page brief. That process takes **3–6 hours per submission**, across 40–60 submissions per week. Quality varies by individual. Reasoning is never documented. When experts leave, institutional knowledge walks out the door.

Most AI tools fail here because they **summarise instead of reason** — they extract facts without applying domain logic, hallucinate with confidence, and offer no way for experts to correct them.

---

## What ORACLE Does Differently

ORACLE doesn't just read documents — it **thinks through them in discrete, auditable steps**, like a junior underwriter who shows all their work to a senior reviewer:

1. Researches the company *(web enrichment, public filings, news signals)*
2. Decomposes the analysis into **5 expert reasoning modules**
3. Reasons through each module independently with domain-specific logic
4. **Scores its own confidence** (HIGH / MEDIUM / LOW) per section
5. Presents a structured brief with expandable reasoning traces
6. **Learns from expert corrections** through a built-in evaluation loop

---

## Live Demo

🔗 **Try ORACLE on Streamlit Cloud →** *(link after deployment)*

🎬 **2-min Loom Walkthrough →** *(link after recording)*

---

## Example Output

<details>
<summary><strong>📄 Click to expand: ORACLE Brief for Acme Manufacturing Corp</strong></summary>

```
═══════════════════════════════════════════════════════════
 ORACLE UNDERWRITING BRIEF
 Company: Acme Manufacturing Corp
 SIC: 3490 — Misc. Fabricated Metal Products
 Date: 2026-03-09 | Run ID: abc-123 | ORACLE v0.1
═══════════════════════════════════════════════════════════

[Section 1: Risk Profile]                    Confidence: HIGH ██
Industry: Light manufacturing, fabricated metal products
Risk Type: Mixed — Property + Casualty
Key Characteristics:
  • Heavy machinery operation → equipment breakdown exposure
  • Raw material storage → fire/environmental risk
  • Skilled labor dependency → workers' comp considerations
Red Flags: None identified from public data.
▶ Show ORACLE's reasoning (6 steps)

[Section 2: Financial Signals]             Confidence: MEDIUM ██
Revenue: $84.2M (2024) vs $95.1M (2023) — declining 11.5%
Industry Benchmark: SIC 3490 avg growth +2.1%
Classification: NEGATIVE financial signal
Underwriting Rule Applied: Revenue decline >10% = heightened scrutiny
⚠ Data Gap: No Q3/Q4 2024 update available
▶ Show ORACLE's reasoning (6 steps)

[Section 3: Operational Exposure]          Confidence: HIGH ██
...

[Section 4: Loss History Indicators]       Confidence: LOW ██
⚠ No public loss runs available — actual loss runs required before binding.
...

[Section 5: Recommendation]                Confidence: MEDIUM ██
Appetite: REFER TO UNDERWRITER
Primary Concerns: Revenue decline, limited loss data
...

═══════════════════════════════════════════════════════════
 RQS Pending — Submit your evaluation below
═══════════════════════════════════════════════════════════
```

</details>

---

## How It Works

```
┌──────────────────┐
│   Company Name   │  ← User inputs a company name
└────────┬─────────┘
         ▼
┌──────────────────────┐
│  Context Enrichment  │  ← Web search → profile, industry, news, financials
└────────┬─────────────┘
         ▼
┌──────────────────────┐
│ Decomposition Engine │  ← Breaks analysis into 5 independent reasoning tasks
└────────┬─────────────┘
         ▼
┌──────────────────────────────────────────────────────┐
│       Domain Reasoning Layer (5 parallel modules)    │
│                                                      │
│  Risk Profile │ Financial │ Operational │ Loss │ Rec  │
│  Each module: observe → classify → apply rules → conclude
└────────┬─────────────────────────────────────────────┘
         ▼
┌──────────────────────┐
│   Validation Gate    │  ← Confidence scoring, source attribution,
│                      │     contradiction detection
└────────┬─────────────┘
         ▼
┌──────────────────────┐
│  Structured Output   │  ← Professional brief + expandable reasoning traces
└────────┬─────────────┘
         ▼
┌──────────────────────┐
│ Evaluation Module    │  ← Per-section approve / edit / reject → RQS score
└──────────────────────┘     → feedback stored → prompts improve
```

The key insight: each module is a **separate LLM call** with a domain-specific prompt and chain-of-thought. It's like having five specialist analysts who each write their section independently, then a senior reviewer checks the whole brief. That's very different from asking one model to "write an underwriting brief" in a single shot.

---

## What Makes This Different

| Feature | ORACLE | Typical AI Wrapper |
|---|---|---|
| **Reasoning trace** | Every section shows step-by-step logic | Black box |
| **Confidence scoring** | HIGH / MEDIUM / LOW per section with source quality | "Here's your answer" |
| **Human-in-the-loop** | Approve / Edit / Reject per section | Accept or start over |
| **Evaluation built in** | RQS metric tracks quality over time | No feedback loop |
| **Partial regeneration** | Re-run one section without restarting | All or nothing |

---

## Product Decisions I Made (And Why)

**1. Five separate LLM calls instead of one big prompt.**
A single prompt asking "write an underwriting brief" is like asking one person to be an expert in five different things simultaneously. Breaking it into modules means each prompt can be deeply specialised, and if one section is wrong, you only regenerate that section — not the whole brief.

**2. Confidence scoring is mandatory, not optional.**
Most AI tools bury their uncertainty. ORACLE forces every section to declare HIGH / MEDIUM / LOW confidence with a reason. An underwriter reading a LOW-confidence section knows to do their own research. An underwriter reading a HIGH-confidence section from a tool that never expresses doubt? That's dangerous.

**3. The evaluation panel is a first-class feature, not an afterthought.**
RQS (Reasoning Quality Score) isn't just a metric — it's the mechanism through which ORACLE improves. Every approve/edit/reject decision teaches the system what "good" looks like. Think of it like how a teacher's red-ink corrections are more valuable than a pass/fail grade.

**4. No document upload in MVP — deliberately.**
The MVP proves the *reasoning pattern* using publicly available company data. Adding document upload is a parsing problem, not a reasoning problem. Ship the reasoning first, prove it works, then add document ingestion in V1.

---

## Tech Stack

| Layer | Technology | Why |
|---|---|---|
| **LLM Reasoning** | Claude API (`claude-sonnet-4-6`) | Best-in-class document reasoning + structured output |
| **Web Enrichment** | Tavily API | Real-time company data in structured JSON |
| **Backend** | Python + FastAPI | Fast async, great for chained LLM calls |
| **Database** | SQLite (MVP) → PostgreSQL (V1+) | Zero setup for MVP, production-ready path forward |
| **Frontend** | Streamlit (MVP) → React + TypeScript (V1) | Ship in hours, then full HITL control |
| **Evaluation** | LLM-as-Judge (V1) + Vector Store (V2) | Automated quality scoring → self-improving loop |

---

## Project Structure

```
oracle/
├── README.md
├── requirements.txt
├── .env.example
│
├── api/
│   ├── main.py                   # FastAPI entry point
│   ├── models.py                 # Pydantic schemas
│   ├── database.py               # SQLite connection + queries
│   └── routes/
│       ├── runs.py               # POST /runs, GET /runs/{id}
│       ├── sections.py           # PATCH /runs/{id}/sections
│       └── feedback.py           # POST /runs/{id}/feedback
│
├── pipeline/
│   ├── enrichment.py             # Company data fetch (Tavily)
│   ├── decomposer.py             # Break input into 5 reasoning tasks
│   ├── reasoning.py              # Per-module LLM reasoning calls
│   ├── validator.py              # Confidence scoring + source attribution
│   ├── formatter.py              # Structured output assembly
│   └── evaluator.py              # RQS computation + feedback logging
│
├── prompts/
│   ├── system.py                 # Base persona prompt
│   ├── risk_profile.py           # Module 1
│   ├── financial_signals.py      # Module 2
│   ├── operational_exposure.py   # Module 3
│   ├── loss_indicators.py        # Module 4
│   └── recommendation.py         # Module 5
│
├── frontend/
│   └── app.py                    # Streamlit app (MVP)
│
├── data/
│   └── oracle.db                 # SQLite database
│
└── tests/
    ├── test_pipeline.py
    └── test_cases/               # Ground-truth company briefs
```

---

## What's Deliberately Not in This Version

| Feature | Why Not Yet |
|---|---|
| **Document upload** | MVP proves the reasoning pattern on public data first |
| **User authentication** | Single-user demo — auth adds complexity without insight |
| **PDF export** | Markdown export proves value; PDF is a V1 polish item |
| **Multiple domains** | Insurance is the beachhead; portability is a V2 architecture bet |
| **Batch processing** | One-at-a-time proves quality before scaling throughput |
| **Fine-tuned models** | Prompt engineering first — fine-tuning is a V2 optimisation |

Being explicit about what you *didn't* build is just as important as showing what you did.

---

## Roadmap

### V1 — Scale the Foundation *(Weeks 3–6)*

- PDF document upload and parsing *(the leap from demo → real tool)*
- Multi-source reasoning with contradiction detection
- React frontend with real-time reasoning trace expansion
- Knowledge Base input for firm-specific underwriting rules
- Side-by-side comparison mode *(run ORACLE on two companies)*
- Professional PDF export
- Evaluation dashboard with aggregate RQS trends

### V2 — Generalise the Pattern *(Months 2–4)*

- **Domain Abstraction Layer** — insurance, legal, clinical, support as configurations
- **Dynamic Context Injection** — vector store of approved outputs for few-shot retrieval
- **REST API** — expose the reasoning pipeline as infrastructure
- **Graduated Autonomy** — modules earn auto-approval through demonstrated accuracy
- **Batch Processing** — 50+ submissions via API

---

## The Transferable Pattern

ORACLE is built for insurance. But the architecture — *structured reasoning over complex documents + human oversight + evaluation loop* — is the same pattern behind Harvey (legal), Abridge (clinical), Sierra (customer resolution), and Decagon (support agents).

The domain changes. The pattern doesn't.
