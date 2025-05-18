from models.load_chat_model import load_model
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_ans():
    ans_prompt=PromptTemplate(
        input_variables=["input_text","questions"],
        template=open("prompts/answers_prompt.txt").read()
    )
    return LLMChain(
        llm=load_model(),
        prompt=ans_prompt
    )