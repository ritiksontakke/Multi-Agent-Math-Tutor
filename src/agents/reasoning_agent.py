from src.config.llm import llm
from langchain.tools import tool
from langchain.agents import create_agent

reasoning_agent = create_agent(
    model=llm,
    system_prompt="""
You are a Reasoning Agent.

Extract values from the math problem.

Return ONLY valid JSON.

Example:
{
  "operation": "compound_interest",
  "principal": 10000,
  "rate": 8,
  "time": 3
}

Do not explain.
Do not calculate.
Do not add markdown.
"""
)