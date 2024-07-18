from transformers import AutoTokenizer, AutoModelForCausalLM

# 加载 GPT 模型
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

class GPTModel:
    def __init__(self):
        self.tokenizer = tokenizer
        self.model = model

    async def extract_keywords(self, text):
        prompt = f"Extract keywords from the following text: {text}"
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=50)
        keywords = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return keywords

    async def generate_response(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=500)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

gpt = GPTModel()

async def extract_gpt_keywords(text):
    return await gpt.extract_keywords(text)

async def generate_gpt_response(prompt):
    return await gpt.generate_response(prompt)
