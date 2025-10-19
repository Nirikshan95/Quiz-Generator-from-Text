import os
from pydantic import BaseModel, Field,SecretStr
from typing import Annotated
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from output_parser.quiz_parser import OptionedQuiz
from quiz_generation.quiz_gen import create_quiz

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
    text: Annotated[str,Field(...,description="Text to generate quiz from")] 
    api_key: Annotated[SecretStr,Field(...,description="Huggingface API Key for authentication")]

class QuizResponse(BaseModel):
    quiz: list[OptionedQuiz]


# API Endpoints

@app.get("/")
async def root():
    return {"message": "Welcome to the QuizGen API!"}

@app.post(
    "/create_quiz/",
    description="Generate a quiz from the provided text.",
    response_model=QuizResponse
    )
async def generate_quiz(request: QuizRequest):
    try:
        os.environ["HUGGINGFACEHUB_API_TOKEN"]=request.api_key.get_secret_value()
        os.environ["HF_TOKEN"]=request.api_key.get_secret_value()
        result= create_quiz(request.text)
        quiz=result.quiz_out
        
        if not quiz:
            raise HTTPException(status_code=500, detail="Quiz generation failed.")
        
        return QuizResponse(quiz=quiz)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.environ.pop("HUGGINGFACEHUB_API_TOKEN", None)
        os.environ.pop("HF_TOKEN", None)
        