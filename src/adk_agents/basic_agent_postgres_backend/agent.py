import asyncio
from google.adk.agents.llm_agent import Agent 
from google.adk.sessions import DatabaseSessionService 

# 1. Declare your session storage backend independently
postgres_session_service = DatabaseSessionService( 
    db_url="postgresql+asyncpg://postgres:secret@localhost:5432/adk_testing" 
) 

# 2. Keep the Agent declaration completely bare of connection objects
root_agent = Agent( 
    model='gemini-2.5-flash', 
    name='root_agent', 
    description='A helpful assistant for user questions.', 
    instruction='Answer user questions to the best of your knowledge', 
)

# 3. Explicit schema generator loop
async def init_db():
    print("Initializing ADK database tables...")
    await postgres_session_service.prepare_tables()
    print("Database tables validated/created successfully!")

if __name__ == "__main__":
    asyncio.run(init_db())
