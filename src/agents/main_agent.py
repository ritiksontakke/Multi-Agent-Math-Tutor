from src.config.llm import llm
from langchain.agents import create_agent

# src/agents/main_agent.py

import json

from src.tools.subagent_tools import (
    call_reasoning_agent,
    call_calculator_agent,
    call_reviewer_agent
)

print("step 1")
def main_agent(question: str):
    print("\nSTEP 2: Main Agent Started")
    print("\nSTEP 3: Calling Reasoning Agent")
    reasoning_result = call_reasoning_agent.invoke(
        {"query": question}
    )
    
    reasoning_result = json.loads(reasoning_result)

    calculation_result = call_calculator_agent.invoke(
        {"query": json.dumps(reasoning_result)}
    )
    print("\nSTEP 4: Reasoning Agent Completed")
    print("\nSTEP 5: Calling Calculator Agent")

    calculation_result = json.loads(calculation_result)

    review_result = call_reviewer_agent.invoke(
        {
            "query": json.dumps(
                {
                    "reasoning": reasoning_result,
                    "calculation": calculation_result
                }
            )
        }
    )
    print("\nSTEP 6: Calculator Agent Completed")
    print("\nSTEP 7: Calling Reviewer Agent")

    review_result = json.loads(review_result)
    print("\nSTEP 8: Reviewer Agent Completed")

    return {
        "reasoning_agent": reasoning_result,
        "calculator_agent": calculation_result,
        "reviewer_agent": review_result
    }