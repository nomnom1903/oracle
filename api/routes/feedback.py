from fastapi import APIRouter, HTTPException
from api.models import Feedback

router = APIRouter()


@router.post("/{run_id}/feedback", response_model=Feedback, status_code=201)
def submit_feedback(run_id: int, feedback: Feedback):
    """Submit analyst feedback for a run or specific section."""
    # TODO: validate run exists, persist feedback, update RQS
    raise HTTPException(status_code=501, detail="Not implemented")
