import openai
from openai import OpenAI
from backend.config import config

openai.api_key = config.OPENAI_API_KEY
client = OpenAI()

def extract_gpt_keywords(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Extract keywords from the following text: {text}"}
        ]
    )
    keywords = response.choices[0].message.content.strip()

    return keywords

def generate_gpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer
