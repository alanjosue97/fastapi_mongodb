from motor.motor_asyncio import AsyncIOMotorClient

async def get_db():
    client = AsyncIOMotorClient("mongodb+srv://academia:Alpe10017Dec@cluster0.mtpqpfb.mongodb.net/?retryWrites=true&w=majority")
    return client.academia