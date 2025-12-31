from fastapi import APIRouter
from app.services.nlp_service import analyze_text

router = APIRouter()

@router.post("/sentiment")
def sentiment(payload: dict):
    text = payload.get("text", "")
    return analyze_text(text)
