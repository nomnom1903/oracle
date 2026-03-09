from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Run(BaseModel):
    id: Optional[int] = None
    document_name: str
    status: str = "pending"
    rqs_score: Optional[float] = None
    created_at: Optional[datetime] = None


class Section(BaseModel):
    id: Optional[int] = None
    run_id: int
    module: int
    title: str
    content: str
    confidence: Optional[float] = None
    sources: Optional[str] = None


class Feedback(BaseModel):
    id: Optional[int] = None
    run_id: int
    section_id: Optional[int] = None
    rating: int
    comment: Optional[str] = None
    created_at: Optional[datetime] = None
