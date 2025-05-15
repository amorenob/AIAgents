from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())

# Create a ChatOpenAI model instance
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define a prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an comedian who tells jokes about {topic}."),
        ("human", "Tell me {n} jokes about {topic}."),
    ]
)

chain = prompt_template | model | StrOutputParser()

# Invoke the chain with input values
response = chain.invoke({"n": 3, "topic": "cats"})
print(response)

