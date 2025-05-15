
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

_ = load_dotenv(find_dotenv())

# Initialize the models
openai_model = ChatOpenAI(model="gpt-3.5-turbo")
anthropic_model = ChatAnthropic(model="claude-3-5-sonnet-20241022")
google_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Define the messages
messages = [
    SystemMessage(
        content="You are an assistant who responds in the style of Dr Seuss."
    ),
    HumanMessage(
        content="write me a very short poem about a happy carrot"
    )
]

# Get completions from OpenAI model
response_openai = openai_model(messages)
print("Response from OpenAI model:")
print(response_openai.content)
print("\n" + "="*50 + "\n")

# Get completions from Anthropic model
response_antropic = anthropic_model(messages)
print("Response from Anthropic model:")
print(response_antropic.content)
print("\n" + "="*50 + "\n")

# Get completions from Google model 
gemini_response = google_model(messages)
print("Response from Google model:")
print(gemini_response.content)
print("\n" + "="*50 + "\n")