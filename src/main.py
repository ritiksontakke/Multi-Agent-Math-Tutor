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
    print("STEP 1: Health Check Called")
    return {
        "status": "running"
    }

print("step 2")
@app.post("/solve")
async def solve_math(request: MathRequest):
    print("STEP 1: Request Received")

    return main_agent(
        request.question
    )
print("STEP 10: Response Ready")