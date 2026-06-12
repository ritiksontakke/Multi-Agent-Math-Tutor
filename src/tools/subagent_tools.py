# tools/subagent_tools.py

from langchain.tools import tool
from src.config.llm import llm
from src.agents.reasoning_agent import reasoning_agent
from src.agents.calculator_agent import calculator_agent
from src.agents.reviewer_agent import reviewer_agent

@tool
def call_reasoning_agent(query: str) -> str:
    """Solve mathematical and logical reasoning problems.

    Use this skill when the user needs:
    - Arithmetic calculations
    - Algebra, geometry, calculus, or statistics solutions
    - Step-by-step mathematical reasoning
    - Logic puzzles and analytical problem solving
    - Complex reasoning that requires detailed explanation

    Returns the reasoning agent's final answer with explanations.
    """
    result = reasoning_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query,
                }
            ]
        }
    )

    return result["messages"][-1].content

@tool
def call_calculator_agent(
    query : str
):
    """ call_calculator_agent """

    result = calculator_agent.invoke(
        {
            "messages" : [
                {
                    "role" : "user",
                    "content" : query
                }
            ]
        }
    )

    return result["messages"][-1].content

@tool
def call_reviewer_agent(
    query: str
):
    """Review answers"""

    result = reviewer_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    return result["messages"][-1].content