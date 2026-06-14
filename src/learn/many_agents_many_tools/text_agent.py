from langchain.tools import tool
from langchain.agents import create_agent
from utils import get_groq_model, get_system_prompt

@tool("word_count")
def word_count(text: str) -> int:
    """
    Count the total number of words in the provided text.

    Use this tool when the user asks for the number of words
    in a sentence, paragraph, or document.

    Args:
        text: The input text.

    Returns:
        The total word count.
    """
    return len(text.split())

@tool("character_count")
def character_count(text: str) -> int:
    """
    Count the total number of characters in the provided text.

    Use this tool when the user asks for the character count
    of a sentence, paragraph, or document.

    Args:
        text: The input text.

    Returns:
        The total number of characters, including spaces.
    """
    return len(text)

@tool("uppercase")
def uppercase(text: str) -> str:
    """
    Convert all characters in the provided text to uppercase.

    Use this tool when the user wants text transformed
    into capital letters.

    Args:
        text: The input text.

    Returns:
        The text converted to uppercase.
    """
    return text.upper()

@tool("lowercase")
def lowercase(text: str) -> str:
    """
    Convert all characters in the provided text to lowercase.

    Use this tool when the user wants text transformed
    into lowercase letters.

    Args:
        text: The input text.

    Returns:
        The text converted to lowercase.
    """
    return text.lower()

@tool("reverse_text")
def reverse_text(text: str) -> str:
    """
    Reverse the order of characters in the provided text.

    Use this tool when the user wants to reverse text.

    Args:
        text: The input text.

    Returns:
        The reversed text.
    """
    return text[::-1]

@tool("remove_extra_spaces")
def remove_extra_spaces(text: str) -> str:
    """
    Remove leading, trailing, and repeated spaces from text.

    Use this tool to clean and normalize text formatting.

    Args:
        text: The input text.

    Returns:
        Cleaned text with normalized spacing.
    """
    return " ".join(text.split())

@tool("get_text_agent")
def get_text_agent(query: str):
    """
    Handle text-processing user requests by delegating them
    to a specialized Text Agent.

    Use this tool when the query involves text transformations,
    word or character counting, text reversal, case conversion,
    or text formatting operations.

    Args:
        query (str): The user's text-related request.

    Returns:
        str: The Text Agent's response containing the processed
        text or requested text analysis.
    """

    text_agent = create_agent(
            model = get_groq_model(),
            tools=[word_count, character_count, uppercase, lowercase, reverse_text, remove_extra_spaces],
            system_prompt=get_system_prompt("project01_text_agent"),
        )
    result = text_agent.invoke({"messages": [{"role": "user", "content": query}]})
    return result["messages"][-1].content

# Example usage
if __name__ == "__main__":
    sample_text = "  Hello   World  "

    print("Word Count:", word_count(sample_text))
    print("Character Count:", character_count(sample_text))
    print("Uppercase:", uppercase(sample_text))
    print("Lowercase:", lowercase(sample_text))
    print("Reversed:", reverse_text(sample_text))
    print("Cleaned:", remove_extra_spaces(sample_text))