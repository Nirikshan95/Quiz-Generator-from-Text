from langchain_core.prompts import PromptTemplate
from models.load_chat_model import get_chat_model
from output_parser.quiz_parser import parse_quiz

def create_quiz(text):
    """
    The function `create_quiz` takes a text input, creates a quiz parser, sets up a prompt template, and
    then invokes a chain of operations to generate a quiz based on the input text.
    
    :param text: The `create_quiz` function seems to be a part of a larger codebase related to creating
    quizzes. It appears to take a text input and then processes it through a chain of operations
    involving a quiz parser, a prompt template, and a chat model to generate a quiz
    :return: The function `create_quiz(text)` takes a text input, creates a quiz parser, sets up a
    prompt template for the quiz, and then invokes a chain of operations involving the quiz prompt, chat
    model, and quiz parser. Finally, it returns the result of invoking this chain with the input text
    provided.
    """
    quiz_parser=parse_quiz()
    qns_prompt=PromptTemplate(
        input_variables=["input_text"],
        template=open("./prompts/quiz_prompt.txt").read(),
        partial_variables={"format_instructions":quiz_parser.get_format_instructions()}
    )
    model = get_chat_model()
    if model is None:
        raise RuntimeError("Chat model not available; check get_chat_model()")
    chain = qns_prompt | model | quiz_parser
    return chain.invoke({"input_text":text})

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

    
if __name__ == "__main__":
    input_text = input("Enter the text to generate questions from: ")
    result = create_quiz(input_text)
    print(result)
    #post_process(result)
    #print(result.quiz_out)
    