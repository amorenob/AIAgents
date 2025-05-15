from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain.prompts import ChatPromptTemplate

_ = load_dotenv(find_dotenv())
model = ChatOpenAI(model="gpt-3.5-turbo")

print("Prompt templates")
prompt_template = ChatPromptTemplate.from_template(
    "Tell me a {adjetive} jokes about {topic}."
)

prompt = prompt_template.invoke({"adjetive": "funny", "topic": "dogs"})
print(prompt)

ai_response = model.invoke(prompt)
print(ai_response.content)