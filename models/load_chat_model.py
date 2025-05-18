from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import os
from configs.config import MODEL_REPO_ID,TEMPERATURE,MAX_TOKENS

def load_model(model_repo_id=MODEL_REPO_ID,temperature=TEMPERATURE,max_tokens=MAX_TOKENS):
    
    return ChatHuggingFace(
        llm=HuggingFaceEndpoint(
            repo_id=model_repo_id,
            temperature=temperature,
            max_new_tokens=max_tokens,
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
            )
        )