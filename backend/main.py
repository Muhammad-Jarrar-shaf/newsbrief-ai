from fastapi import FastAPI

from backend.api.summarize import router


app = FastAPI(
    title="NewsBrief AI",
    description="AI-powered news article summarizer",
    version="1.0.0",
)

app.include_router(router)