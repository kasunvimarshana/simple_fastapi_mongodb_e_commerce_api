import beanie
from motor.motor_asyncio import AsyncIOMotorClient
from .Entity import Entity
from .Folder import Folder

models = [Entity, Folder]

async def init_beanie():
    client = AsyncIOMotorClient("mongo-uri")

    # Entity.update_forward_refs(Folder=Folder)
    Entity.model_rebuild(Folder=Folder)
    
    await beanie.init_beanie(database=client["mongo-db-name"], document_models=models)