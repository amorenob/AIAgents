from dotenv import load_dotenv, find_dotenv

from langchain_openai import  ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage

_ = load_dotenv(find_dotenv())

# model

model = ChatOpenAI(model="gpt-3.5-turbo")

system_message = SystemMessage(content="You are a helpful assistant.")


def get_feedback_template(sentiment:str) -> ChatPromptTemplate:
    if sentiment == "escalate":
        human_message = ("human", "Generate a message to escalate this feedback to a human agent {feedback}.")
    else:
        human_message = ("human", "Generate a thank you note for this" + sentiment +  "feedback {feedback}.")
        
    return ChatPromptTemplate.from_messages(
        [
            system_message,
            human_message
        ]
    )

def create_pmo_chain(template:ChatPromptTemplate, model):
    return template | model | StrOutputParser

# Define classification template
classification_template = ChatPromptTemplate.from_messages(
    [
        system_message,
        ("human", "Classify the sentiment of this feedback as positive, negative, neutral, or escalate:{feedback}")
    ]
)

branches = RunnableBranch(
    (lambda x: "positive" in x, get_feedback_template("positive") | model | StrOutputParser()),
    (lambda x: "negative" in x, get_feedback_template("negative") | model | StrOutputParser()),
    (lambda x: "neutral" in x, get_feedback_template("neutral") | model | StrOutputParser()),
    get_feedback_template("escalate") | model | StrOutputParser(), # default branch
)

clasification_chain = classification_template | model | StrOutputParser()

chain = clasification_chain | branches

review = "Im not sure about the product yet, can your escalate"
result = chain.invoke(review)
print(result)
