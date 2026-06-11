# tools/subagent_tools.py

from langchain.tools import tool
from src.config.llm import llm
from src.agents.reasoning_agent import reasoning_agent
from src.agents.calculator_agent import calculator_agent
from src.agents.reviewer_agent import reviewer_agent
@tool
def call_reasoning_agent(
    query : str
):
    """ Analyze math problems """

    result = reasoning_agent.invoke(
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