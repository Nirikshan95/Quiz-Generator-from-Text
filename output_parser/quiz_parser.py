from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from typing import List, Literal

# This Python class `OptionedQuiz` defines a model for a quiz question with multiple options and the
# index of the correct answer.
class OptionedQuiz(BaseModel):
    question:str=Field(description="The question to be answered.")
    options:list[str]=Field(description="The options to be answered.")
    answer_index:int=Field(description="The index of the correct option.")
    
class BlanksQuiz(BaseModel):
    question:str=Field(description="The question to be answered.")
    answers_list:list[str]=Field(description="The list of correct answers.")
    
class TorFQuiz(BaseModel):
    question:str=Field(description="The question to be answered.")
    answer:bool=Field(description="The answer to the question (True or False).")
    
class OrderingQuiz(BaseModel):
    question:str=Field(description="The question to be answered.")
    contents:list[str]=Field(...,description="The list of contents to be ordered.")
    answer_index_list:list[int]=Field(...,description="The list of index numbers representing the correct order of contents.")
    
class MatchingQuiz(BaseModel):
    left_contents:List[str]=Field(...,description="The list of left side contents.")
    right_contents:List[str]=Field(...,description="The list of right side contents.")
    answer_index_list:list[int]=Field(...,description="The list of index numbers representing the correct matches from the right contents.")
    
# The `Quiz` class defines a list of questions with options and correct answer index numbers.
class QuizWithOptionsList(BaseModel):
    quiz_out:List[OptionedQuiz]=Field(description="A list of questions with options and correct answer index number")
class QuizWithBlanksList(BaseModel):
    quiz_out:List[BlanksQuiz]=Field(description="A list of questions with blanks and correct answers")
class TrueFalseQuizList(BaseModel):
    quiz_out:List[TorFQuiz]=Field(description="A list of True/False questions with correct answers")
class OrderingQuizList(BaseModel):
    quiz_out:List[OrderingQuiz]=Field(description="A list of ordering questions with correct order index lists")
class MatchingQuizList(BaseModel):
    quiz_out:List[MatchingQuiz]=Field(description="A list of matching questions with correct match index lists")


def parse_quiz(quiz_type:Literal["optioned_quiz","blanks_quiz","true_false_quiz","ordering_quiz","matching_quiz"]) -> PydanticOutputParser:
    """
    The function `parse_quiz` returns a PydanticOutputParser object with a Pydantic Quiz object.
    :return: An instance of PydanticOutputParser with the pydantic_object set to Quiz.
    """
    if quiz_type=="optioned_quiz":
        return PydanticOutputParser(pydantic_object=QuizWithOptionsList)
    elif quiz_type=="blanks_quiz":
        return PydanticOutputParser(pydantic_object=QuizWithBlanksList)
    elif quiz_type=="true_false_quiz":
        return PydanticOutputParser(pydantic_object=TrueFalseQuizList)
    elif quiz_type=="ordering_quiz":
        return PydanticOutputParser(pydantic_object=OrderingQuizList)
    elif quiz_type=="matching_quiz":
        return PydanticOutputParser(pydantic_object=MatchingQuizList)

