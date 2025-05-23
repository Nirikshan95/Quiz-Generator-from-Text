import sys
from langchain.prompts import PromptTemplate
sys.path.append("./")
from models.load_chat_model import get_chat_model
from output_parser.quiz_parser import parse_quiz

def create_quiz(text):
    quiz_parser=parse_quiz()
    qns_prompt=PromptTemplate(
        input_variables=["input_text"],
        template=open("./prompts/quiz_prompt.txt").read(),
        partial_variables={"format_instructions":quiz_parser.get_format_instructions()}
    )
    print("Loaded chat model...")
    chain=  qns_prompt|get_chat_model()|quiz_parser
    return chain.invoke({"input_text":text})

def post_process(result,index=0):
    first_question = result.quiz_out[index]
    return first_question.question, first_question.options, first_question.answer_index

    
if __name__ == "__main__":
    input_text = input("Enter the text to generate questions from: ")
    result = create_quiz(input_text)
    post_process(result)
    #print(result.quiz_out)
    
    '''The capital of France is Paris. It is known for its art, fashion, and culture. The Eiffel Tower is one of its most famous landmarks. The Louvre Museum is also located in Paris and is home to thousands of works of art, including the Mona Lisa. Paris is a major European city and a global center for art, fashion, and culture. It is known for its cafe culture, and landmarks like the Eiffel Tower, Notre-Dame Cathedral, and the Louvre Museum. The city has a rich history and is often referred to as the 'City of Light'.'''