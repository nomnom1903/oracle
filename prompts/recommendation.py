RECOMMENDATION_PROMPT = """
## Module 5 — Recommendation

Synthesise findings from all prior modules into a final, actionable recommendation.

Your output must include:
1. **Summary of Key Findings** — 3–5 bullet points drawing on Modules 1–4.
2. **Overall Assessment** — a single verdict: Proceed / Proceed with Conditions / Decline / Escalate.
3. **Recommended Actions** — specific next steps for the analyst or decision-maker.
4. **Residual Uncertainties** — what remains unknown and how it affects confidence.
5. **Reasoning Quality** — self-assess the completeness and reliability of this analysis.

The recommendation must be grounded in evidence from the document and enrichment data.
Do not introduce new facts at this stage — only synthesise what has already been established.
""".strip()
