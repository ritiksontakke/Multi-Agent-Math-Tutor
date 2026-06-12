from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.main_agent import main_agent
app = FastAPI()


class MathRequest(BaseModel):
    user_id: str
    question: str


@app.get("/")
def health_check():
    return {"status": "running"}


@app.post("/solve")
async def solve_math(request: MathRequest):

    return main_agent(
        user_id=request.user_id,
        question=request.question
    )