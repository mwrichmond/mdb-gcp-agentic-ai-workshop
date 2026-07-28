from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool
from .custom_functions import get_fx_rate
from .custom_agents import google_search_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    tools=[
        FunctionTool(get_fx_rate),
        AgentTool(agent=google_search_agent),
    ]
)
