from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain.prompts import ChatPromptTemplate

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())

# Create a ChatOpenAI model instance
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define a prompt template
promtp_template = ChatPromptTemplate.from_template(
    "Tell me a {adjetive} jokes about {topic}."
)

promp = promtp_template.invoke({"adjetive":"funny","topic": "dogs"})
print(promp)

messages = [
    ("system", "You are an assistant who responds in the style of {person}."),
    ("human", "Tell me a funny joke about {topic}."),
]
# Create a ChatPromptTemplate instance
chat_prompt = ChatPromptTemplate.from_messages(messages)
prompt = chat_prompt.invoke({"person": "Dr Seuss", "topic": "cats"})
print(prompt)