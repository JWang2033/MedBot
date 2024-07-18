# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("stanford-crfm/BioMedLM")
model = AutoModelForCausalLM.from_pretrained("stanford-crfm/BioMedLM")

class MedBotModel:
    def __init__(self):
        self.tokenizer = tokenizer
        self.model = model

    def predict(self, question):
        # 编码输入问题
        inputs = self.tokenizer.encode(question, return_tensors='pt')

        # 使用模型生成响应
        outputs = self.model.generate(inputs, max_length=500)

        # 解码生成的响应
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

medbot = MedBotModel()

def predict_medical_response(question):
    return medbot.predict(question)