# Import required packages and modules
# from __future__ import annotations
# import logging as logging
# import sys as sys
# import os as os
# import platform as platform
# import psutil as psutil
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
import app.configs.database as database
from app.configs.Setting import Setting as Setting
from app.utils.Logger import Logger as Logger
# import schemas
from app.schemas.HealthResource import HealthResource as HealthResourceSchema
# import controllers
from app.controllers.ApplicationController import ApplicationController as ApplicationController

router = APIRouter()
application_controller = ApplicationController()

@router.get(
        "/applications/check-health", 
        response_model=Optional[HealthResourceSchema], 
        status_code=status.HTTP_200_OK, 
        dependencies=[]
    )
async def check_health(
        db: AsyncIOMotorDatabase = Depends(database.get_database)
    ) -> Optional[HealthResourceSchema]:
        response = await application_controller.check_health(db)
        return response


__all__ = [
    "router"
]
