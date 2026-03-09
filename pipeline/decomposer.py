"""
Decomposer module — breaks the input document into 5 structured reasoning tasks.

Each task maps to one of ORACLE's reasoning modules:
  1. Risk Profile
  2. Financial Signals
  3. Operational Exposure
  4. Loss Indicators
  5. Recommendation
"""


def decompose(document_text: str) -> list[dict]:
    """Split a document into 5 module-specific reasoning tasks.

    Args:
        document_text: Raw text of the submitted document.

    Returns:
        A list of 5 task dicts, each with 'module', 'title', and 'context'.
    """
    # TODO: extract relevant passages per module, build task payloads
    raise NotImplementedError
