from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import sys
from configs import config
import os
from dotenv import load_dotenv
load_dotenv()
def get_chat_model():
    """
    The function `get_chat_model` returns a ChatHuggingFace model with specified parameters.
    :return: An instance of the ChatHuggingFace class with the specified parameters llm, repo_id,
    temperature, max_new_tokens, and huggingfacehub_api_token is being returned.
    """
    try:
        llm=HuggingFaceEndpoint(
        repo_id=config.MODEL_REPO_ID,
        temperature=config.TEMPERATURE,
        max_new_tokens=config.MAX_TOKENS
        #huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )
        return ChatHuggingFace(llm=llm)
    except Exception as e:
        print(f"Error initializing model: {e}")
        return None
