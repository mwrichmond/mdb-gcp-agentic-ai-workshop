import asyncio
import os

# Clear, direct namespaces validated against the ADK source architecture
from google.adk import Agent
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+asyncpg://postgres:secret@localhost:5432/adk_testing"
)

async def main():
    my_agent = Agent(
        name="SessionSupportAgent",
        model="gemini-2.5-flash",
        instruction="You are a helpful assistant.",
    )

    # Validated: DatabaseSessionService accepts db_url
    session_service = DatabaseSessionService(db_url=DATABASE_URL)

    runner = Runner(
        agent=my_agent,
        app_name="my_support_app",
        session_service=session_service,
    )

    # Validated via open issues: create_session takes flat string keywords directly
    session = await session_service.create_session(
        app_name="my_support_app",
        user_id="user_12345",
        session_id="unique_chat_uuid_abc"
    )
    
    # The session object exposes details directly via attributes (.id, .app_name)
    print(f"Successfully generated persistent Session ID: {session.id}")

if __name__ == "__main__":
    asyncio.run(main())
