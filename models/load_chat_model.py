from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint,HuggingFacePipeline
import sys
sys.path.append("./")
from configs import config
import os

'''def get_chat_model():
    try:
        llm=HuggingFacePipeline.from_model_id(
        model_id=config.MODEL_REPO_ID,
        task="text-generation",
        model_kwargs={
            "temperature": config.TEMPERATURE,
            "max_new_tokens": config.MAX_TOKENS,
            "token": os.getenv("HUGGINGFACEHUB_API_TOKEN")
        },
        )
        return ChatHuggingFace(llm=llm)
    except Exception as e:
        print(f"Error initializing model: {e}")'''
        
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
        max_new_tokens=config.MAX_TOKENS,
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )
        return ChatHuggingFace(llm=llm)
    except Exception as e:
        print(f"Error initializing model: {e}")
if __name__ == "__main__":
    chat_model = get_chat_model()
    print(chat_model)
    input="Hello, how are you?"
    result=chat_model.invoke(input)
    print(result)