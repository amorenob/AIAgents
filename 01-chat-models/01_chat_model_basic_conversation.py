from dotenv import load_dotenv, find_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())
# Create a ChatOpenAI model instance
model = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    SystemMessage(
        content="You are an assisttant who responds in the style of Dr Seuss."
    ),
    HumanMessage(
        content="write me a very short poem about a happy carrot"
    ),
]

# invoke the model
response = model.invoke(messages)

#print(f"Answer from OpenAI API: {response.content}")

messages = [
    SystemMessage(
        content="You are an assisttant who responds in the style of Dr Seuss."
    ),
    HumanMessage(
        content="write me a very short poem about a happy carrot"
    ),
    AIMessage(
        content=response.content
    ),
    HumanMessage(
        content="Now change carrot to potato"
    ),
    
]

# invoke the model
response = model.invoke(messages)
print(f"Answer from OpenAI API: {response.content}")