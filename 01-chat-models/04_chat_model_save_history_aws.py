
# basic
from dotenv import load_dotenv, find_dotenv

# langchain
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_community.chat_message_histories import (
    DynamoDBChatMessageHistory,
)

# AWS
import boto3

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())

# Check if DinamoDB table exists
def check_dynamodb_table_exists(table_name):
    dynamodb = boto3.client("dynamodb")
    try:
        response = dynamodb.describe_table(TableName=table_name)
        return True
    except dynamodb.exceptions.ResourceNotFoundException:
        return False
    except Exception as e:
        print(f"Error checking table existence: {e}")
        return False

TABLE_NAME = "chat-history"
if not check_dynamodb_table_exists(TABLE_NAME):
    print(f"DynamoDB table '{TABLE_NAME}' does not exist.")
    print("Creating table...")
    
    dynamodb = boto3.resource("dynamodb")
    
    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                "AttributeName": "SessionId",
                "KeyType": "HASH",  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "SessionId",
                "AttributeType": "S",  # String type
            },
        ],
        BillingMode="PAY_PER_REQUEST",
    )
    
    # Wait until the table exists.
    table.meta.client.get_waiter("table_exists").wait(TableName=TABLE_NAME)
    print(f"Table '{TABLE_NAME}' created successfully.")
else:
    print(f"DynamoDB table '{TABLE_NAME}' already exists.")
    

chat_history = DynamoDBChatMessageHistory(
    table_name=TABLE_NAME,
    session_id="1",  # Replace with your session ID
)

system_message = SystemMessage(
    content="You are an assistant who responds in the style of Master Yoda."
)

if not chat_history.messages:
    # If the chat history is empty, add the system message
    chat_history.add_message(system_message)

# Create a ChatOpenAI model instance
model = ChatOpenAI(model="gpt-3.5-turbo")
# Create a SystemMessage instance

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    # Create a HumanMessage instance
    human_message = HumanMessage(content=user_input)
    chat_history.add_message(human_message)

    # Get the model's response
    response = model.invoke(chat_history.messages)
    
    chat_history.add_message(response)

    # Print the model's response
    print(f"AI: {response.content}")

