from langchain.agents import load_tools
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent

import os

base_path = os.environ.get('OPENAI_API_BASE', 'http://localhost:8080/v1')
key = os.environ.get('OPENAI_API_KEY', '-')
model_name = os.environ.get('MODEL_NAME', 'gpt-3.5-turbo')

chat = ChatOpenAI(temperature=0.7, openai_api_base=base_path, openai_api_key=key, model_name=model_name)
# llm = OpenAI(temperature=0.7, openai_api_base=base_path, openai_api_key=key, model_name=model_name)

# Make sure you sign up for serp api and set you environment variable SERPAPI_API_KEY
search = SerpAPIWrapper()
tools = load_tools(["serpapi", "llm-math"], llm=chat)

memory = ConversationBufferMemory(memory_key="chat_history")

agent_chain = initialize_agent(tools, chat, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory, handle_parsing_errors=False)

if __name__ == "__main__":
    print("You are now chatting with the AI. Type 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'quit':
            break
        else:
            response = agent_chain.run(user_input)
            print("AI: ", response)