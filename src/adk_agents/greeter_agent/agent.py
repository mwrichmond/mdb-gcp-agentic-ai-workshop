from google.adk.agents.llm_agent import Agent

def greetings(query: str):
  """Tool to greet user."""
  if 'hello' in query.lower():
    return {"greeting": "Hello, world"}
  else:
    return {"greeting": "Goodbye, world"}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='my_agent',
    description='A helpful assistant for user questions.',
    instruction="You are an Agent that greet users, always use greetings tool to respond.",
    tools=[greetings]
)
