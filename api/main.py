from fastapi import FastAPI
from api.routes import runs, sections, feedback

app = FastAPI(title="ORACLE API", description="AI Document Reasoning Engine")

app.include_router(runs.router, prefix="/runs", tags=["runs"])
app.include_router(sections.router, prefix="/runs", tags=["sections"])
app.include_router(feedback.router, prefix="/runs", tags=["feedback"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
