import os
from pydantic import BaseModel, Field,SecretStr
from typing import Annotated,Literal,List
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from output_parser.quiz_parser import QuizWithOptionsList,QuizWithBlanksList,TrueFalseQuizList,OrderingQuizList,MatchingQuizList
from quiz_generation.quiz_gen import create_quiz_chain

app=FastAPI(title="QuizGen API", version="1.0.0")

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # need to change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Schemas
class QuizRequest(BaseModel):
    text: Annotated[str,Field(...,description="Text/topic to generate quiz from")] 
    level: Annotated[Literal["easy", "medium", "hard"],Field(...,description="Difficulty level of the quiz")]
    past_quiz_qns: Annotated[list[str],Field(...,description="List of past quiz questions to avoid repetition")]
    api_key: Annotated[SecretStr,Field(...,description="Huggingface API Key for authentication")]

class MatchingQuizRequest(BaseModel):
    text: Annotated[str,Field(...,description="Text/topic to generate matching quiz from")] 
    level: Annotated[Literal["easy", "medium", "hard"],Field(...,description="Difficulty level of the matching quiz")]
    past_quiz_qns: Annotated[List[List[List[str]]],Field(...,description="List of past quiz questions to avoid repetition")]
    api_key: Annotated[SecretStr,Field(...,description="Huggingface API Key for authentication")]

# ---------------------------------------------------------------

# API Endpoints

@app.get("/")
async def root():
    return {"message": "Welcome to the QuizGen API!"}

@app.post(
    "/create_mcqs/",
    description="Generate a multiple choice quiz from the provided text.",
    response_model=QuizWithOptionsList
    )

async def generate_mcqs(request: QuizRequest):
    try:
        os.environ["HUGGINGFACEHUB_API_TOKEN"]=request.api_key.get_secret_value()
        os.environ["HF_TOKEN"]=request.api_key.get_secret_value()
        quiz_chain= create_quiz_chain(quiz_type="optioned_quiz")
        result = await quiz_chain.ainvoke({"level":request.level,"input_text":request.text,"past_questions":request.past_quiz_qns})
        quiz=result.quiz_out
        

        
        if not quiz:
            raise HTTPException(status_code=500, detail="Quiz generation failed.")
        
        return QuizWithOptionsList(quiz_out=quiz)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.environ.pop("HUGGINGFACEHUB_API_TOKEN", None)
        os.environ.pop("HF_TOKEN", None)
        
@app.post(
    "/create_fill_blanks/",
    description="Generate a fill in the blanks quiz from the provided text.",
    response_model=QuizWithBlanksList
    )

async def generate_fill_in_blanks(request: QuizRequest):
    try:
        os.environ["HUGGINGFACEHUB_API_TOKEN"]=request.api_key.get_secret_value()
        os.environ["HF_TOKEN"]=request.api_key.get_secret_value()
        quiz_chain= create_quiz_chain(quiz_type="blanks_quiz")
        result = await quiz_chain.ainvoke({"level":request.level,"input_text":request.text,"past_questions":request.past_quiz_qns})
        quiz=result.quiz_out
        

        
        if not quiz:
            raise HTTPException(status_code=500, detail="Quiz generation failed.")
        
        return QuizWithBlanksList(quiz_out=quiz)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.environ.pop("HUGGINGFACEHUB_API_TOKEN", None)
        os.environ.pop("HF_TOKEN", None)

@app.post(
    "/create_true_or_false_quiz/",
    description="Generate a True/False quiz from the provided text.",
    response_model=TrueFalseQuizList
    )

async def generate_true_false_quiz(request: QuizRequest):
    try:
        os.environ["HUGGINGFACEHUB_API_TOKEN"]=request.api_key.get_secret_value()
        os.environ["HF_TOKEN"]=request.api_key.get_secret_value()
        quiz_chain= create_quiz_chain(quiz_type="true_false_quiz")
        result = await quiz_chain.ainvoke({"level":request.level,"input_text":request.text,"past_questions":request.past_quiz_qns})
        quiz=result.quiz_out
        

        
        if not quiz:
            raise HTTPException(status_code=500, detail="Quiz generation failed.")
        
        return TrueFalseQuizList(quiz_out=quiz)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.environ.pop("HUGGINGFACEHUB_API_TOKEN", None)
        os.environ.pop("HF_TOKEN", None)
        
@app.post(
    "/create_ordering_quiz/",
    description="Generate a ordering quiz from the provided text.",
    response_model=OrderingQuizList
    )

async def generate_ordering_quiz(request: QuizRequest):
    try:
        os.environ["HUGGINGFACEHUB_API_TOKEN"]=request.api_key.get_secret_value()
        os.environ["HF_TOKEN"]=request.api_key.get_secret_value()
        quiz_chain= create_quiz_chain(quiz_type="ordering_quiz")
        result = await quiz_chain.ainvoke({"level":request.level,"input_text":request.text,"past_questions":request.past_quiz_qns})
        quiz=result.quiz_out
        

        
        if not quiz:
            raise HTTPException(status_code=500, detail="Quiz generation failed.")
        
        return OrderingQuizList(quiz_out=quiz)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.environ.pop("HUGGINGFACEHUB_API_TOKEN", None)
        os.environ.pop("HF_TOKEN", None)
        
        
@app.post(
    "/create_matching_quiz/",
    description="Generate a matching quiz from the provided text.",
    response_model=MatchingQuizList
    )

async def generate_matching_quiz(request: MatchingQuizRequest):
    try:
        os.environ["HUGGINGFACEHUB_API_TOKEN"]=request.api_key.get_secret_value()
        os.environ["HF_TOKEN"]=request.api_key.get_secret_value()
        quiz_chain= create_quiz_chain(quiz_type="matching_quiz")
        result = await quiz_chain.ainvoke({"level":request.level,"input_text":request.text,"past_questions":request.past_quiz_qns})
        quiz=result.quiz_out
        

        
        if not quiz:
            raise HTTPException(status_code=500, detail="Quiz generation failed.")
        
        return MatchingQuizList(quiz_out=quiz)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.environ.pop("HUGGINGFACEHUB_API_TOKEN", None)
        os.environ.pop("HF_TOKEN", None)