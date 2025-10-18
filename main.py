from fastapi import FastAPI
from fastapi.responses import JSONResponse
from quiz_generation.quiz_gen import create_quiz, post_process

app=FastAPI(title="QuizGen API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Welcome to the QuizGen API!"}
# Endpoint to create a quiz
@app.post("/create_quiz/")
async def generate_quiz(test: str):
    result= create_quiz(test)
    quiz=result.quiz_out
    print("Raw Quiz:\n\n", quiz)
    return JSONResponse(content={"quiz": [quiz_item.dict() for quiz_item in quiz]})