import openai
from backend.config import config

openai.api_key = config.OPENAI_API_KEY

class GPTModel:
    def __init__(self):
        self.api_key = config.OPENAI_API_KEY

    async def extract_keywords(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Extract keywords from the following text: {text}"}
            ]
        )
        keywords = response['choices'][0]['message']['content']
        return keywords

    async def generate_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return answer

gpt = GPTModel()

async def extract_gpt_keywords(text):
    return await gpt.extract_keywords(text)

async def generate_gpt_response(prompt):
    return await gpt.generate_response(prompt)

