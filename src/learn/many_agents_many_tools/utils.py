from langchain_groq import ChatGroq
from langsmith import Client

import os
from dotenv import load_dotenv
load_dotenv()

client = Client()

def get_groq_model():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )

def get_system_prompt(prompt_name: str, tag: str = "production") -> str:
    prompt = client.pull_prompt(f"{prompt_name}:{tag}")
    return prompt.messages[0].prompt.template