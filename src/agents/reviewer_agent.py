from src.config.llm import llm
from langchain.agents import create_agent

reviewer_agent = create_agent(
    model=llm,
    system_prompt="""
You are a Reviewer Agent.

Verify the result.

Return ONLY valid JSON.

Example:
{
  "status": "verified",
  "final_answer": 12597.12
}

No explanation.
No markdown.
"""
)