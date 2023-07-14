from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7, model_name="text-davinci-003")

# Create a prompt template with limited options
template = "Choose a color: {Red}, {Green}, or {Blue}"
input_vars = {"Red": "Red", "Green": "Green", "Blue": "Blue"}

prompt = PromptTemplate(template=template, input_variables=input_vars)

# Initialize the LLMChain
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Provide a question and run the LLMChain
question = "What is your favorite color?"
llm_chain.run(question)