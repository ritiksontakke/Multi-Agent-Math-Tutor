import json

from src.memory.memory_manager import (
    save_message,
    get_history
)

from src.tools.subagent_tools import (
    reasoning_agent,
    calculator_agent,
    reviewer_agent
)


def main_agent(
    user_id: str,
    question: str
):
    print("========== MAIN AGENT STARTED ==========")

    # Load user history
    history = get_history(user_id)

    # Handle memory questions directly
    memory_questions = [
        "what is my previous question",
        "what was my previous question",
        "what was my last question",
        "what did i ask before",
        "show my last question",
        "what is my last message",
        "what was my last message"
    ]


    if question.lower().strip() in memory_questions :

        return {
            "user_id": user_id,
            "history": history
        }

    # Save current user message
    save_message(
        user_id=user_id,
        role="user",
        content=question
    )

    print("STEP 1: Calling Reasoning Agent")

    reasoning_result = reasoning_agent.invoke(
        {
            "query": question,
            "history": history
        }
    )

    try:
        if isinstance(reasoning_result, str):
            reasoning_result = json.loads(reasoning_result)
    except Exception:
        return {
            "error": "Reasoning Agent returned invalid JSON",
            "response": reasoning_result
        }

    print("STEP 2: Calling Calculator Agent")

    calculation_result = calculator_agent.invoke(
        {
            "query": json.dumps(reasoning_result)
        }
    )

    try:
        if isinstance(calculation_result, str):
            calculation_result = json.loads(calculation_result)
    except Exception:
        return {
            "error": "Calculator Agent returned invalid JSON",
            "response": calculation_result
        }

    print("STEP 3: Calling Reviewer Agent")

    review_result = reviewer_agent.invoke(
        {
            "query": json.dumps(
                {
                    "reasoning": reasoning_result,
                    "calculation": calculation_result
                }
            )
        }
    )

    try:
        if isinstance(review_result, str):
            review_result = json.loads(review_result)
    except Exception:
        return {
            "error": "Reviewer Agent returned invalid JSON",
            "response": review_result
        }

    final_response = {
        "reasoning_agent": reasoning_result,
        "calculator_agent": calculation_result,
        "reviewer_agent": review_result
    }

    # Save assistant response
    save_message(
        user_id=user_id,
        role="assistant",
        content=json.dumps(final_response)
    )

    print("STEP 4: Response Saved To Memory")
    print("========== MAIN AGENT FINISHED ==========")

    return final_response