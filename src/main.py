from fastapi import FastAPI
from pydantic import BaseModel

from src.agents.main_agent import main_agent

app = FastAPI(
    title="Math Tutor Multi-Agent API"
)


class MathRequest(BaseModel):
    question: str


@app.get("/")
def health_check():
    return {
        "status": "running"
    }


from src.agents.main_agent import main_agent

@app.post("/solve")
async def solve_math(request: MathRequest):

    return main_agent(
        request.question
    )