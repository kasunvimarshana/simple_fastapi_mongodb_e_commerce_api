from functools import lru_cache
from typing import TYPE_CHECKING, \
    Annotated
from fastapi import Depends, FastAPI
from .Setting import Setting

app = FastAPI()

@lru_cache
def get_settings():
    return Settings()

@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "PROJECT_NAME": settings.PROJECT_NAME
    }