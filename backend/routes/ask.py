from fastapi import APIRouter, Request
from backend.models.medbot import get_diagnosis, extract_medbot_keywords
from backend.gpt.gpt_model import extract_gpt_keywords, generate_gpt_response

router = APIRouter()

@router.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data['question']

    # get keyword using GPT
    gpt_keywords = await extract_gpt_keywords(question)

    # diagnosis by medbot
    diagnosis = get_diagnosis(gpt_keywords)

    # form natural language response using GPT
    response = await generate_gpt_response(f"Q: {question}\nDiagnosis: {diagnosis}\nA:")

    return {"response": response}
