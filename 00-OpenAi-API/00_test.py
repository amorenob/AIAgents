from dotenv import load_dotenv, find_dotenv
import os
import openai
import requests
import json




# Load environment variables from .env file
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completions(messages, 
                     model="gpt-3.5-turbo",
                     temperature=0,
                     max_tokens=100):
    """
    Get completions from OpenAI API.
    Args:
        messages (list): List of messages to send to the model.
        model (str): Model to use for completion.
        temperature (float): Sampling temperature.
        max_tokens (int): Maximum number of tokens to generate.
    Returns:
        response (dict): Response from OpenAI API.
    """
    # Check if the API key is set
    if not openai.api_key:
        raise ValueError("API key is not set. Please set the OPENAI_API_KEY environment variable.")
    # Check if the model is valid
    valid_models = ["gpt-3.5-turbo", "gpt-4"]
    if model not in valid_models:
        raise ValueError(f"Invalid model. Please choose from {valid_models}.")
    # Check if the messages are in the correct format
    if not isinstance(messages, list):
        raise ValueError("Messages should be a list.")
    if not all(isinstance(msg, dict) and "role" in msg and "content" in msg for msg in messages):
        raise ValueError("Each message should be a dictionary with 'role' and 'content' keys.")


    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response
# Test the function
messages = [
    {"role": "system", "content": """You are an assistant who\
                                    responds in the style of Dr Seuss."""},
    {"role": "user", "content": """write me a very short poem\
                                    about a happy carrot"""}
]
response = get_completions(messages)

res_dict = response.to_dict()
print("Response from OpenAI API:")
print(json.dumps(res_dict, indent=4))