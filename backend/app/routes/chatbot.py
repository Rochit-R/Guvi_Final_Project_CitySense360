from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_chatbot import ask_city_bot

router = APIRouter(prefix="/chatbot", tags=["City RAG Assistant"])

class ChatQuery(BaseModel):
    question: str

@router.post("/ask")
def chat(query: ChatQuery):
    answer = ask_city_bot(query.question)
    return {"answer": answer}
