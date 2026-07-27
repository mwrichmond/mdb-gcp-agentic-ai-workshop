import asyncio
from google.adk.agents import Agent
# from google.adk.runners import InMemoryRunner (included in Gemini's first attempt at coding, wonderful, huh?)
from google.adk import Runner
from google.adk.sessions import DatabaseSessionService
from adk_database_memory import DatabaseMemoryService

# Define your PostgreSQL connection string
# Ensure you use an async driver like asyncpg for production-grade setups
DATABASE_URL = "postgresql+asyncpg://postgres:secret@localhost:5432/adk_db"

# Initialize Session Service for tracking active conversation history
session_service = DatabaseSessionService(db_url=DATABASE_URL)

# Initialize Memory Service for long-term semantic retrieval across sessions
memory_service = DatabaseMemoryService(db_url=DATABASE_URL)

# Create your ADK agent instance
agent = Agent(
    name="postgres_assistant",
    model="gemini-2.5-flash", # Or your preferred supported model
    instruction="You are a helpful data assistant with access to persistent memory.",
)

async def handle_agent_session(user_id: str, session_id: str, user_message: str):
    # Initialize runner with the persistent services
    runner = Runner(
        agent=agent,
        app_name="enterprise_chat_app",
        session_service=session_service,
        memory_service=memory_service
    )
    
    # Run the single interaction step
    # The runner automatically reads previous blocks from PostgreSQL and saves new state deltas
    response_stream = await runner.run(
        user_id=user_id,
        session_id=session_id,
        message=user_message
    )
    
    async for event in response_stream:
        if event.content:
            print(event.content, end="")

async def manage_sessions():
    app_name = "enterprise_chat_app"
    user_id = "user_12345"

    # List all tracked sessions for a specific user
    active_sessions = await session_service.list_sessions(app_name=app_name, user_id=user_id)
    
    # Delete an expired or closed session to manage data bloat
    await session_service.delete_session(session_id="session_abc123")

# ... (Your previous setup code goes here)

async def main():
    # Example execution payload
    await handle_agent_session(
        user_id="terminal_user_456", 
        session_id="persistent_session_999", 
        user_message="Hello! Remember that my favorite database tool is PostgreSQL."
    )

if __name__ == "__main__":
    # Standard entry point to safely run the async event loop
    asyncio.run(main())

