from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class QNSOutput(BaseModel):
    
    question1:str=Field(description="The question1 to be answered.")
    question2:str=Field(description="The question2 to be answered.")
    question3:str=Field(description="The question3 to be answered.")
    question4:str=Field(description="The question4 to be answered.")
    question5:str=Field(description="The question5 to be answered.")

def parse_qns():
    return PydanticOutputParser(pydantic_object=QNSOutput)