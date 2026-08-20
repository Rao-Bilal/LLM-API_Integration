"""
Stage 0 checkpoint script.
Proves we can talk to the model provider from our own machine.
Run with:  python -m dotenv run -- python src/llm/hello.py
or simply: python src/llm/hello.py   (after `pip install python-dotenv`
           and loading .env, see load_dotenv() below).
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env into os.environ

client = OpenAI(
    base_url=os.environ["LLM_BASE_URL"],  
    api_key=os.environ["LLM_API_KEY"],    
)

res = client.chat.completions.create(
    model=os.environ["LLM_MODEL"],  # e.g. gemma3:1b
    messages=[{"role": "user", "content": "Reply with exactly the word: ready"}],
)

print(res.choices[0].message.content)
