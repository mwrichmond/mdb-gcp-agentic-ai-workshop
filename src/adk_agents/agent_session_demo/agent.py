from google.adk.agents.llm_agent import Agent
from .custom_functions import inspect_live_session
# from .custom_functions import save_variable_tool

root_agent = Agent(
    model='gemini-2.5-flash',
    name='StateDemoAgent',
    instruction=(
        "You are a helpful assistant assisting with a session state demonstration. "
        "Whenever the user asks you to check, view, or print session information, "
        "you MUST execute 'inspect_live_session' tool."
        "Additionally, if the user asks you to remember something, write it to state."
    ),
    tools=[inspect_live_session] 
    # tools=[inspect_session_tool, save_variable_tool] 
)
