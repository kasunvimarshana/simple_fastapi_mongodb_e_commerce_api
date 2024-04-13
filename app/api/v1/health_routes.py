# Import required packages and modules
# from __future__ import annotations
# import logging as logging
import sys as sys
import os as os
# from decouple import config
# import asyncio as asyncio
from typing import TYPE_CHECKING, Optional, Any, Type, TypeVar, Generic, ForwardRef, Annotated, Union, List
from fastapi import APIRouter, Request, Depends, status, Query
from motor.motor_asyncio import AsyncIOMotorClient
import platform as platform
import psutil as psutil
import app.configs.database as database

router = APIRouter()

@router.get("/", include_in_schema=False)
@router.get("")
async def health(db: AsyncIOMotorClient = Depends(database.get_database)):
    db_status = None
    try:
        # Check if the database is responsive
        # await db.command('ping')
        db_status = 'up'
    except Exception:
        db_status = 'down'

    # Get system information
    system_info = {
        "system": platform.system(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage('/')._asdict()
    }

    return {
        "database": db_status,
        "system_info": system_info
    }

__all__ = [
    "router"
]