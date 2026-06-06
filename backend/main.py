from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.api.summarize import router


app = FastAPI(
    title="NewsBrief AI",
    description="AI-powered news article summarizer",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(router)