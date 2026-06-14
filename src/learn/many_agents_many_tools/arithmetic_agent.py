from langchain.tools import tool
from langchain.agents import create_agent
from utils import get_groq_model, get_system_prompt

@tool("add_numbers")
def add(a: int, b: int) -> int:
    """Add two integers and return their sum.

    Use this tool when you need to perform addition on two numbers.

    Args:
        a (int): The first integer operand.
        b (int): The second integer operand.

    Returns:
        int: The sum of a and b.
    """
    return a + b

@tool("subtract_numbers")
def sub(a: int, b: int) -> int:
    """Subtract the second integer from the first and return the result.

    Use this tool when you need to perform subtraction on two numbers.

    Args:
        a (int): The integer to subtract from (minuend).
        b (int): The integer to subtract (subtrahend).

    Returns:
        int: The result of a minus b.
    """
    return a - b

@tool("multiply_numbers")
def mul(a: int, b: int) -> int:
    """Multiply two integers and return their product.

    Use this tool when you need to perform multiplication on two numbers.

    Args:
        a (int): The first integer factor.
        b (int): The second integer factor.

    Returns:
        int: The product of a and b.
    """
    return a * b

@tool("divide_numbers")
def divide(a: int, b: int) -> float:
    """Divide the first integer by the second and return the result.

    Use this tool when you need to perform division on two numbers.
    Note: b must not be zero.

    Args:+
        a (int): The dividend (number to be divided).
        b (int): The divisor (number to divide by). Must be non-zero.

    Returns:
        float: The result of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

@tool("arithmetic_agent")
def get_arithmetic_agent(query: str):
    """
    Handle arithmetic-related user requests by delegating them
    to a specialized Arithmetic Agent.

    Use this tool when the query involves mathematical operations
    such as addition, subtraction, multiplication, or division.

    Args:
        query (str): The user's arithmetic question or calculation request.

    Returns:
        str: The Arithmetic Agent's response containing the calculated result.
    """

    arithmetic_agent = create_agent(
            model = get_groq_model(),
            tools=[add, sub, mul, divide],
            system_prompt=get_system_prompt("project01_date_agent"),
        )
    result = arithmetic_agent.invoke({"messages": [{"role": "user", "content": query}]})
    return result["messages"][-1].content
