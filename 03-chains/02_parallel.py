from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel

# Load env variables
_ = load_dotenv(find_dotenv())

# Create openAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

promp_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert product reviewer"),
        ("human", "List the main features of the product {product_name}")
    ]
)

def analyze_feautures(features, objetive="pros"):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are and expert product reviewer."),
            ("human", "Given these features:{features}, list the " + objetive + " of these features")
        ]
    )
    return pros_template.format_prompt(features=features)


def combine_pros_cons(pros, cons):
    return f"Pros: \n {pros} \n\n Cons:\n {cons}"

pros_branch_chain = (
    RunnableLambda(lambda x: analyze_feautures(x, "pros")) | model | StrOutputParser()
)

cons_branch_chain = (
    RunnableLambda(lambda x: analyze_feautures(x, "cons")) | model | StrOutputParser()
)


chain = (
    promp_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain})
    | RunnableLambda( lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))
)

result = chain.invoke({"product_name":"Macbook Pro"})
print(result)