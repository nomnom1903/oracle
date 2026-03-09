from fastapi import APIRouter, HTTPException
from api.models import Section

router = APIRouter()


@router.patch("/{run_id}/sections")
def update_sections(run_id: int, sections: list[Section]):
    """Update or replace sections for a given run."""
    # TODO: upsert sections into DB
    raise HTTPException(status_code=501, detail="Not implemented")
