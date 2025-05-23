from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from typing import Literal, List

class OptionedQuiz(BaseModel):
    question:str=Field(description="The question to be answered.")
    options:list[str]=Field(description="The options to be answered.")
    answer_index:int=Field(description="The index of the correct option.")
    
class Quiz(BaseModel):
    quiz_out:List[OptionedQuiz]=Field(description="A list of 5 questions with options and correct answer index number")

def parse_quiz():
    print("Parsing quiz...")
    return PydanticOutputParser(pydantic_object=Quiz)

