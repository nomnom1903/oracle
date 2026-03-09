FINANCIAL_SIGNALS_PROMPT = """
## Module 2 — Financial Signals

Analyse the financial indicators present in the document and enrichment data.

Your output must include:
1. **Revenue & Profitability Trends** — direction, magnitude, and period covered.
2. **Liquidity & Solvency Signals** — cash position, debt load, covenant risks.
3. **Red Flags** — any anomalies, restatements, or missing disclosures.
4. **Financial Health Summary** — overall assessment: Strong / Stable / Stressed / Distressed.
5. **Confidence** — note data completeness and any figures that could not be verified.

Reference specific figures and their sources for each signal identified.
""".strip()
