from fastapi import APIRouter
from pydantic import BaseModel
from services.rag_service import ask_question

router = APIRouter()


class SearchRequest(BaseModel):
    question: str
    mode: str = "normal"


@router.post("/chat")
async def chat(request: SearchRequest):
    return ask_question(
        question=request.question,
        mode=request.mode
    )