from fastapi import FastAPI
from .init_beanie import init_beanie

my_app = FastAPI()

@my_app.on_event("startup")
async def init():
    await init_beanie()