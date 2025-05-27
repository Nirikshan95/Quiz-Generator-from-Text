from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from typing import List

# This Python class `OptionedQuiz` defines a model for a quiz question with multiple options and the
# index of the correct answer.
class OptionedQuiz(BaseModel):
    question:str=Field(description="The question to be answered.")
    options:list[str]=Field(description="The options to be answered.")
    answer_index:int=Field(description="The index of the correct option.")
    
# The `Quiz` class defines a list of questions with options and correct answer index numbers.
class Quiz(BaseModel):
    quiz_out:List[OptionedQuiz]=Field(description="A list of questions with options and correct answer index number")

def parse_quiz():
    """
    The function `parse_quiz` returns a PydanticOutputParser object with a Pydantic Quiz object.
    :return: An instance of PydanticOutputParser with the pydantic_object set to Quiz.
    """
    return PydanticOutputParser(pydantic_object=Quiz)

