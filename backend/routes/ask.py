from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.models.medbot import get_diagnosis, extract_medbot_keywords
from backend.gpt.gpt_model import extract_gpt_keywords, generate_gpt_response

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question

    # gpt keyword
    gpt_keywords = extract_gpt_keywords(question)

    # medbot keyword
    medbot_keywords = extract_medbot_keywords(question)

    # find best keyword
    keywords = gpt_keywords if gpt_keywords else medbot_keywords

    # diagnose
    diagnosis = get_diagnosis(keywords)

    # gpt answer
    response = generate_gpt_response(f"Q: {question}\nDiagnosis: {diagnosis}\nA:")

    return {"response": response}
