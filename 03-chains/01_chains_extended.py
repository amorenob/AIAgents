from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda

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

# Define a function to format the response
uppercase_output = RunnableLambda(lambda x: x.upper())
count_output = RunnableLambda(lambda x: f"word count:{len(x.split())}\n{x}")
chain = prompt_template | model | StrOutputParser() | uppercase_output | count_output

# Invoke the chain with input values
response = chain.invoke({"n": 3, "topic": "cats"})
print(response)