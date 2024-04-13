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
# import models
from app.models.User import User as UserModel
from app.models.Review import Review as ReviewModel

router = APIRouter()

@router.get("/users")
async def create_user(db: AsyncIOMotorClient = Depends(database.get_database)):
    async with await db.client.start_session() as session:
        try:
            async with session.start_transaction():
                temp_user = await UserModel.insert_one(UserModel(first_name="First name 1", last_name="Last name 1", email="test1@email.com"), session=session)
                temp_review = await ReviewModel.insert_one(ReviewModel(comment="test comment 1", user=temp_user), session=session)

                temp_user = await UserModel(first_name="First name 2", last_name="Last name 2", email="test2@email.com").create(session=session)
                temp_review = await ReviewModel(comment="test comment 2", user=temp_user).create(session=session)

            # Commit transaction if everything succeeds
            await session.commit_transaction()
            return {"message": "Transfer successful"}

        except Exception as e:
            # Rollback transaction if an error occurs
            await session.abort_transaction()
            print("Error occurred during transfer:", e)


__all__ = [
    "router"
]

