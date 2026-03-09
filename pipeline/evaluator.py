"""
Evaluator module — RQS computation and feedback logging.

Computes the Reasoning Quality Score (RQS) for a completed run based on
section confidence scores, source coverage, and analyst feedback ratings.
Logs evaluation results to the database for longitudinal tracking.
"""


def compute_rqs(sections: list[dict], feedback: list[dict] | None = None) -> float:
    """Compute the Reasoning Quality Score for a run.

    Args:
        sections: Validated section dicts with confidence scores.
        feedback: Optional list of analyst feedback dicts.

    Returns:
        RQS as a float between 0.0 and 1.0.
    """
    # TODO: weighted average of confidence + feedback signal
    raise NotImplementedError


def log_evaluation(run_id: int, rqs: float) -> None:
    """Persist the RQS score to the database.

    Args:
        run_id: The run to update.
        rqs: The computed RQS score.
    """
    # TODO: update runs.rqs_score in DB
    raise NotImplementedError
