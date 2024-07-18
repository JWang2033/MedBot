from fastapi import APIRouter, Request
from backend.models.medbot import predict_medical_response

router = APIRouter()

@router.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data['question']

    # 使用医疗模型进行预测
    medical_response = predict_medical_response(question)

    return {"response": medical_response}
