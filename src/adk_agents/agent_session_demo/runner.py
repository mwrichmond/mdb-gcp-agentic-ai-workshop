import os
import asyncio
from dotenv import load_dotenv

# 1. Load local env
load_dotenv()

# 2. ADK specific content formatting structures
from google.adk.types import Content, Part
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from adk_database_memory import DatabaseMemoryService

# Import the scaffolding instance variable from agent.py
from agent import root_agent 

DB_URI = os.getenv("DATABASE_URI")

async def main():
    session_service = DatabaseSessionService(DB_URI)
    memory_service = DatabaseMemoryService(DB_URI)

    # 3. Create runner override configuration
    runner = Runner(
        app_name="my_app",
        agent=root_agent,
        session_service=session_service,
        memory_service=memory_service
    )
    
    print("Agent runner fixed and active. Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit" or not user_input:
            break
            
        print("Agent: ", end="", flush=True)
        
        # 4. Correct payload wrapping for the ADK SDK execution engine
        user_message = Content(role='user', parts=[Part(text=user_input)])
        
        try:
            # 5. Correct asynchronous execution generator call
            async for event in runner.run_async(
                user_id="matt_richmond",
                session_id="override_test_session_001",
                new_message=user_message
            ):
                # Safely extract text payload chunks out of streamed events
                if hasattr(event, "content") and event.content:
                    for part in event.content.parts:
                        if part.text:
                            print(part.text, end="", flush=True)
                elif hasattr(event, "text") and event.text:
                    print(event.text, end="", flush=True)
        except Exception as e:
            print(f"\n[Execution Error]: {e}")
            
        print() # Line break for next shell entry loop

if __name__ == "__main__":
    asyncio.run(main())

