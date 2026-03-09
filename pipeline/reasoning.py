"""
Reasoning module — per-module LLM reasoning calls via Anthropic Claude.

Each module task is sent to Claude with the ORACLE system prompt and the
appropriate module-specific prompt template. Responses are streamed and
parsed into structured section outputs.
"""


def reason(task: dict, enrichment_context: dict) -> dict:
    """Run a single reasoning module using Claude.

    Args:
        task: A task dict from the decomposer (module, title, context).
        enrichment_context: External data from the enrichment module.

    Returns:
        A dict with 'content', 'confidence', and 'sources'.
    """
    # TODO: build messages, call anthropic client, parse response
    raise NotImplementedError
