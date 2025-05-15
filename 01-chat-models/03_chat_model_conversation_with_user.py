
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())

# Create a ChatOpenAI model instance
model = ChatOpenAI(model="gpt-3.5-turbo")

chat_history = []

system_message = SystemMessage(
    content="You are an assistant who responds in the style of Dr Seuss."
)
chat_history.append(system_message)

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    # Create a HumanMessage instance
    human_message = HumanMessage(content=user_input)
    chat_history.append(human_message)

    # Get the model's response
    response = model.invoke(chat_history)
    chat_history.append(response)

    # Print the model's response
    print(f"AI: {response.content}")
    
print("Chat history:")
print(chat_history)