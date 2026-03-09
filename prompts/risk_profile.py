RISK_PROFILE_PROMPT = """
## Module 1 — Risk Profile

Using the document and any enrichment context provided, construct a structured
risk profile for the entity under analysis.

Your output must include:
1. **Entity Overview** — name, sector, jurisdiction, and business model summary.
2. **Primary Risk Factors** — top 3–5 risks with evidence citations.
3. **Risk Classification** — overall risk tier: Critical / High / Medium / Low.
4. **Confidence** — state your confidence level and explain any data gaps.

Cite the source (document excerpt or enrichment URL) for each risk factor identified.
""".strip()
