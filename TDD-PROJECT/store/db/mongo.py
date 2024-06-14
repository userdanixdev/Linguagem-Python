# Devemos criar um cliente para o mongodb
from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings

class MongoClient:
    def __init__(self)-> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)
    def get(self) -> AsyncIOMotorClient:
        return self.client        
    
db.client = MongoClient()    