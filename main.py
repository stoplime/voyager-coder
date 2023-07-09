from langchain.chat_models import ChatOpenAI

import os

base_path = os.environ.get('OPENAI_API_BASE', 'http://localhost:8080/v1')
key = os.environ.get('OPENAI_API_KEY', '-')
model_name = os.environ.get('MODEL_NAME', 'gpt-3.5-turbo')

llm = ChatOpenAI(temperature=0.7, openai_api_base=base_path, openai_api_key=key, model_name=model_name)

