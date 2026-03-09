"""
Enrichment module — Tavily company data fetch.

Fetches external company intelligence to supplement the input document.
Uses Tavily Search API to retrieve recent news, filings, and market signals
for the entity under analysis. Results are injected into the reasoning context
before pipeline execution begins.
"""


def enrich(company_name: str) -> dict:
    """Fetch enrichment data for a company via Tavily Search.

    Args:
        company_name: The name of the company to research.

    Returns:
        A dict containing news snippets, source URLs, and metadata.
    """
    # TODO: initialise TavilyClient, run search, parse and return results
    raise NotImplementedError
