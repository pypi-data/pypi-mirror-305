import os
import asyncio
from pydantic import BaseModel
from restackio.ai import Restack

class ConnectionOptions(BaseModel):
    engine_id: str
    address: str
    api_key: str

async def main():
    try:
        connection_options = ConnectionOptions(
            engine_id=os.getenv("RESTACK_ENGINE_ID"),
            address=os.getenv("RESTACK_ENGINE_ADDRESS"),
            api_key=os.getenv("RESTACK_ENGINE_API_KEY")
        )

        print("connectionOptions", connection_options.dict())

        restack = Restack(connection_options if os.getenv("RESTACK_ENGINE_API_KEY") else None)

        print("restackClient", restack)
        await restack.start_service({})
        print("Services running successfully.")
    except Exception as e:
        print("Failed to run services", e)

if __name__ == "__main__":
    asyncio.run(main())