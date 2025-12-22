# ai_brain/llm_client.py
from openai import OpenAI

client = OpenAI()

def ask_llm(prompt):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
