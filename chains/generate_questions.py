import sys
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
sys.path.append(".")
from models.load_chat_model import load_model
from output_parser.qns_out import parse_qns

def create_questions(text):
    qns_parse=parse_qns()
    qns_prompt=PromptTemplate(
        input_variables=["input_text"],
        template=open("./prompts/questions_prompt.txt").read(),
        partial_variables={"format_instructions":qns_parse.get_format_instructions()}
    )
    parser=StrOutputParser()
    model=load_model()
    print("Loading model...")
    qns_chain= qns_prompt|model|parser|qns_parse
    return qns_chain.invoke({"input_text":text})
    
if __name__ == "__main__":
    input_text = "The capital of France is Paris. It is known for its art, fashion, and culture. The Eiffel Tower is one of its most famous landmarks. The Louvre Museum is also located in Paris and is home to thousands of works of art, including the Mona Lisa. Paris is a major European city and a global center for art, fashion, and culture. It is known for its cafe culture, and landmarks like the Eiffel Tower, Notre-Dame Cathedral, and the Louvre Museum. The city has a rich history and is often referred to as the 'City of Light'."
    result = create_questions(input_text)
    print(result)