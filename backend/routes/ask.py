from fastapi import APIRouter, Request
from backend.models.medbot import get_diagnosis
from backend.gpt.gpt_model import extract_gpt_keywords, generate_gpt_response

router = APIRouter()

@router.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data['question']

    # 使用 GPT 提取关键词
    keywords = await extract_gpt_keywords(question)

    # 使用 MedBot 生成诊断
    diagnosis = get_diagnosis(keywords)

    # 使用 GPT 生成自然语言回答
    response = await generate_gpt_response(f"Q: {question}\nDiagnosis: {diagnosis}\nA:")

    return {"response": response}
