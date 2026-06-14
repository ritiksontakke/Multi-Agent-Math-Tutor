from langchain.tools import tool
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

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

    Args:
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

#  main code

from langchain.agents import create_agent


class Main:

    user_query : str

    def __init__(self, user_query: str = "what is 2+2"):
        self.user_query = user_query

    def get_llm(self):
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0
        )

    def get_orch_agent(self, system_prompt: str):
        return create_agent(
            model = self.get_llm(),
            tools=[add, sub, mul, divide],
            system_prompt=system_prompt,
        )
    
    def get_prompt(self) -> str:
        from langsmith import Client

        client = Client()
        prompt = client.pull_prompt("main_agent:production")
        system_message = prompt.messages[0].prompt.template
        return system_message

    
    def main(self):
        system_prompt = self.get_prompt()
        agent = self.get_orch_agent(system_prompt=system_prompt)
        result = agent.invoke({"messages": [{"role": "user", "content": self.user_query}]})
        res = result["messages"][-1].content
        print("res : ", res)
    
if __name__ == "__main__":
    user_query = "what is 12*17 and 100+7 and 16-3 and 786 / 2"
    main = Main(user_query);
    main.main()