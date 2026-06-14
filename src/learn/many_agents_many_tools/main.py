from langchain.agents import create_agent
from utils import get_groq_model, get_system_prompt
from arithmetic_agent import get_arithmetic_agent
from date_agent import get_date_agent
from text_agent import get_text_agent

class Orchestrator:

    query : str

    def __init__(self, query:str):
        self.query = query

    def get_orchestrator_agent(self):
        # tools = [add, sub, mul, divide, current_date, current_time, days_between, add_days, is_leap_year, word_count, character_count, uppercase, lowercase, reverse_text, remove_extra_spaces]
        return create_agent(
            model = get_groq_model(),
            tools=[get_arithmetic_agent, get_date_agent, get_text_agent],
            system_prompt=get_system_prompt("project01_orchestrator_agent"),
        )

    def execute_agent(self):
            orchestrator_agent = self.get_orchestrator_agent()
            result = orchestrator_agent.invoke({"messages": [{"role": "user", "content": self.query}]})
            return result["messages"][-1].content

if __name__ == "__main__":
        query = "What day of the week will it be 30 days from today, multiply 15 by 8, and then convert the result sentence The answer is 120 to uppercase.?"
        # query = "Calculate 2 * 2, then add 4 to it. After that, add the previous result to itself. Then add the new result to the previous result. Keep repeating this process until you are sure the answer is complete. you must execute the tools requried loop is file"
        orchestrator = Orchestrator(query)
        result = orchestrator.execute_agent()
        print(f"\n result : {result} \n")
        # python src/learn/many_agents_many_tools/main.py 
        
# TODO:
# model fallback
# max tool call limit
# opt : time limit
# max retry