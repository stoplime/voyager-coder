from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os

base_path = os.environ.get('OPENAI_API_BASE', 'http://localhost:8080/v1')
key = os.environ.get('OPENAI_API_KEY', '-')
model_name = os.environ.get('MODEL_NAME', 'gpt-3.5-turbo')

llm = ChatOpenAI(temperature=0.7, openai_api_base=base_path, openai_api_key=key, model_name=model_name)

if __name__ == "__main__":
    print("You are now chatting with the AI. Type 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'quit':
            break
        else:
            response = llm.predict(user_input, max_tokens=2000)
            print("AI: ", response)
