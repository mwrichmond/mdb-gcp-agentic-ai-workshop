import asyncio
from adk_database_memory import DatabaseMemoryService

# Standard PostgreSQL connection string (postgresql+asyncpg dialect)
memory = DatabaseMemoryService("postgresql+asyncpg://postgres:secret@localhost:5432/adk_testing")

async def main():
    async with memory:
        print("Inserting fact directly into Postgres...")
        
        # FIX: Provide a standard Python dictionary instead of importing custom memory objects
        await memory.add_memory(
            app_name="my_app",
            user_id="u1",
            entry={
                "content": "We decided on a tiered subscription pricing model for the app.",
                "author": "user"
            }
        )
        print("Fact successfully written.")

        print("\nQuerying Postgres memory...")
        result = await memory.search_memory(
            app_name="my_app",
            user_id="u1",
            query="what did we decide about the pricing model?",
        )
        
        # Read directly from the memories object
        if not result.memories:
            print("No matching records found.")
        for entry in result.memories:
            print(f"Found Memory: {entry.content}")

if __name__ == "__main__":
    asyncio.run(main())

