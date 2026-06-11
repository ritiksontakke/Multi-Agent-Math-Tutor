from src.config.llm import llm
from langchain.agents import create_agent

calculator_agent = create_agent(
    model=llm,
    system_prompt="""
You are a Calculator Agent.

Perform calculations only.

Return ONLY valid JSON.

Example:
{
  "amount": 12597.12,
  "compound_interest": 2597.12
}

No explanation.
No markdown.
"""
)