from langchain_core.prompts import PromptTemplate
from models.load_chat_model import get_chat_model
from output_parser.quiz_parser import parse_quiz

def create_quiz_chain():
    """
    The function `create_quiz_chain` generates a chatbot chain for creating a quiz based on provided
    text and past questions.
    
    :param text: The `text` parameter in the `create_quiz_chain` function is a string that represents
    the text or content of the quiz. This text will be used as input for creating the quiz chain
    :type text: str
    :param past_questions: The `past_questions` parameter in the `create_quiz_chain` function is a list
    of strings that stores the questions that have already been asked in the quiz. This parameter is
    optional and has a default value of an empty list `[]`. It is used to keep track of the questions
    that have been
    :type past_questions: list[str]
    :return: The function `create_quiz_chain` returns a chain of components that includes a prompt
    template for a quiz question, a chat model, and a quiz parser.
    """
    
    quiz_parser=parse_quiz()
    qns_prompt=PromptTemplate(
        input_variables=["input_text","past_questions"],
        template=open("./prompts/quiz_prompt.txt").read(),
        partial_variables={"format_instructions":quiz_parser.get_format_instructions()}
    )
    model = get_chat_model()
    if model is None:
        raise RuntimeError("Chat model not available; check get_chat_model()")
    chain = qns_prompt | model | quiz_parser
    return chain

def post_process(result,index=0):
    """
    The function `post_process` extracts question, options, and answer index from a quiz result.
    
    :param result: The `result` parameter seems to be an object that contains a property or method
    called `quiz_out`, which is likely an array or list of quiz objects. The `index` parameter is an
    optional parameter that specifies the index of the quiz object within the `quiz_out` array that you
    want to
    :param index: The `index` parameter in the `post_process` function is used to specify the index of
    the quiz question in the `result.quiz_out` list that you want to process. By default, if no index is
    provided, it will process the quiz question at index 0, defaults to 0 (optional)
    :return: The function `post_process` takes a `result` object and an optional `index` parameter. It
    then retrieves the quiz at the specified index from the `result` object and returns the question,
    options, and answer index of that quiz.
    """
    quiz = result.quiz_out[index]
    return quiz.question, quiz.options, quiz.answer_index