# Import required packages and modules
# from __future__ import annotations
# import logging as logging
# import sys as sys
# import os as os
import platform as platform
import psutil as psutil
# from decouple import config
# import asyncio as asyncio 
from typing import TYPE_CHECKING, \
    Optional, \
    Any, \
    Union, \
    Type, \
    TypeVar, \
    Generic, \
    ForwardRef, \
    Annotated, \
    List
from fastapi import APIRouter, Request, Depends, HTTPException, status, Body, Query
# import pymongo as pymongo
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from datetime import datetime, timezone
import app.configs.database as database
from app.configs.Setting import Setting as Setting
from app.utils.Logger import Logger as Logger
# import schemas
from app.schemas.HealthResource import HealthResource as HealthResourceSchema

class ApplicationService:
    def __init__(self):
        self.settings = Setting()
        self.logger = Logger(__name__)

    async def check_health(
            self, 
            db: AsyncIOMotorDatabase
        ) -> Optional[HealthResourceSchema]:
            self.logger.debug("check_health called")
            db_status: str = None
            system_info: dict = dict()
            try:
                system_info = {
                    "system": platform.system(),
                    "processor": platform.processor(),
                    "architecture": platform.architecture(),
                    "memory": psutil.virtual_memory()._asdict(),
                    "disk": psutil.disk_usage('/')._asdict()
                }
                await db.command("ping")
                db_status = "up"
            except Exception:
                db_status = "down"

            return HealthResourceSchema.parse_obj({**system_info, db_status: db_status})


__all__ = [
    "ApplicationService"
]