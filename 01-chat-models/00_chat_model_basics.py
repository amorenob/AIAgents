
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

_ = load_dotenv(find_dotenv())

model = ChatOpenAI(model="gpt-3.5-turbo")

# invoke the model
response = model.invoke(
    "You are an assistant who responds in the style of Dr Seuss. "
    "write me a very short poem about a happy carrot"
)
print("Full Response from OpenAI API:")
print(response)
print("Content Only")
print(response.content)
print("Message Only")