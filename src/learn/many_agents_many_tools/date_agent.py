from langchain.tools import tool
from datetime import datetime, timedelta
from langchain.agents import create_agent
from utils import get_groq_model, get_system_prompt

@tool("current_date")
def current_date() -> str:
    """
    Get the current date.

    Use this tool when the user asks for today's date.

    Returns:
        The current date in YYYY-MM-DD format.
    """
    return datetime.now().strftime("%Y-%m-%d")

@tool("current_time")
def current_time() -> str:
    """
    Get the current local time.

    Use this tool when the user asks for the current time.

    Returns:
        The current time in HH:MM:SS format.
    """
    return datetime.now().strftime("%H:%M:%S")

@tool("days_between")
def days_between(start_date: str, end_date: str) -> int:
    """
    Calculate the number of days between two dates.

    Use this tool when the user wants to know the duration
    between two dates.

    Args:
        start_date: Start date in YYYY-MM-DD format.
        end_date: End date in YYYY-MM-DD format.

    Returns:
        The number of days between the dates.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return abs((end - start).days)

@tool("add_days")
def add_days(date: str, days: int) -> str:
    """
    Add a specified number of days to a date.

    Use this tool when the user wants a future or past date.

    Args:
        date: Base date in YYYY-MM-DD format.
        days: Number of days to add. Negative values subtract days.

    Returns:
        The resulting date in YYYY-MM-DD format.
    """
    base_date = datetime.strptime(date, "%Y-%m-%d")
    new_date = base_date + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")

@tool("day_of_week")
def day_of_week(date: str) -> str:
    """
    Determine the day of the week for a given date.

    Args:
        date: Date in YYYY-MM-DD format.

    Returns:
        The day name (e.g., Monday, Tuesday).
    """
    dt = datetime.strptime(date, "%Y-%m-%d")
    return dt.strftime("%A")

@tool("is_leap_year")
def is_leap_year(year: int) -> bool:
    """
    Check whether a given year is a leap year.

    Args:
        year: The year to check.

    Returns:
        True if the year is a leap year, otherwise False.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

@tool("get_date_agent")
def get_date_agent(query: str):
    """
    Handle date and time related user requests by delegating them
    to a specialized Date Agent.

    Use this tool when the query involves dates, times, durations,
    calendar calculations, day lookups, or leap year checks.

    Args:
        query (str): The user's date or time related question.

    Returns:
        str: The Date Agent's response containing the requested
        date or time information.
    """
    date_agent = create_agent(
            model = get_groq_model(),
            tools=[current_date, current_time, days_between, add_days, is_leap_year],
            system_prompt=get_system_prompt("project01_date_agent"),
        )
    result = date_agent.invoke({"messages": [{"role": "user", "content": query}]})
    return result["messages"][-1].content


# Example usage
if __name__ == "__main__":
    print("Current Date:", current_date())
    print("Current Time:", current_time())
    print("Days Between:", days_between("2026-01-01", "2026-12-31"))
    print("Add Days:", add_days("2026-06-14", 30))
    print("Day of Week:", day_of_week("2026-06-14"))
    print("Leap Year:", is_leap_year(2028))