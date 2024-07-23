from transformers import AutoTokenizer, AutoModelForCausalLM

class MedBotModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def extract_keywords(self, text):
        # 这里可以实现一个简单的关键词提取算法
        inputs = self.tokenizer.encode(text, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=50)
        keywords = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return keywords

    def diagnose(self, keywords):
        # 模拟的诊断结果
        return f"Diagnosis based on keywords: {keywords}"

medbot = MedBotModel(model_name="gpt2")

def get_diagnosis(keywords):
    return medbot.diagnose(keywords)

def extract_medbot_keywords(text):
    return medbot.extract_keywords(text)
