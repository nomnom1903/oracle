from fastapi import APIRouter, HTTPException
from api.models import Run

router = APIRouter()


@router.post("/", response_model=Run, status_code=201)
def create_run(run: Run):
    """Submit a new document for reasoning analysis."""
    # TODO: persist to DB, trigger pipeline
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{run_id}", response_model=Run)
def get_run(run_id: int):
    """Retrieve a run by ID including its sections."""
    # TODO: fetch run + sections from DB
    raise HTTPException(status_code=501, detail="Not implemented")
