import asyncio
from google.cloud.alloydb.connector import AsyncConnector, IPTypes

async def test_connection():
    try:
        connector = AsyncConnector()
        print("Attempting IAM connection via impersonated credentials...")
        conn = await connector.connect(
            "projects/matt-richmond/locations/us-central1/clusters/alloydb-test-cluster/instances/alloydb-test-cluster-primary",
            "asyncpg",
            user="adk-agent@matt-richmond.iam",
            db="adk_testing",
            enable_iam_auth=True,
            ip_type=IPTypes.PUBLIC
        )
        print("Success! Connection established.")
        await conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")

asyncio.run(test_connection())
