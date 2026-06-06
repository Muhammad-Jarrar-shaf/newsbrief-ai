from fastapi import APIRouter, HTTPException

from backend.schemas.summarize_schema import SummarizeRequest
from backend.services.pipeline_service import summarize_from_url

router = APIRouter()


@router.post("/summarize")
def summarize(request: SummarizeRequest):

    try:
        result = summarize_from_url(str(request.url))

        return {
            "summary": result["summary"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )