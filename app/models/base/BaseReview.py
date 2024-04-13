# Import required packages and modules
# from __future__ import annotations
# import logging as logging
# import sys as sys
# import os as os
# from decouple import config
# import asyncio as asyncio 
from typing import TYPE_CHECKING, \
    Optional, \
    Any, \
    Union, \
    List
# import pymongo as pymongo
from beanie import Document, Indexed, PydanticObjectId, Link, BackLink, before_event, after_event, Insert, Replace, Before, After
from pydantic import Field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from bson import ObjectId
from decimal import Decimal
from faker import Faker

fake = Faker()

class BaseReview(Document):
    # _id: Optional[UUID] = Field(
    #         # default=None, 
    #         description="_id", 
    #         default_factory=uuid4
    #     )
    # _id: Optional[PydanticObjectId] = Field(
    #         default=None, 
    #         description="_id"
    #     )
    _id: Optional[PydanticObjectId] = None
    # user_id: Optional[PydanticObjectId] = Field(
    #         default=None, 
    #         description="user_id"
    #     )
    # product_id: Optional[PydanticObjectId] = Field(
    #         default=None, 
    #         description="product_id"
    #     )
    rate_value: Optional[float] = Field(
            default=0, 
            description="rate_value"
        )
    comment: Optional[str] = Field(
            default=None, 
            description="comment"
        )
    is_toxic_comment: Optional[bool] = Field(
            default=False, 
            description="is_toxic_comment"
        )
    created_at: Optional[datetime] = Field(
            # default=None, 
            description="created_at", 
            default_factory=datetime.now
        )
    updated_at: Optional[datetime] = Field(
            # default=None, 
            description="updated_at", 
            default_factory=datetime.now
        )
    ip_address: Optional[str] = Field(
            default=None, 
            description="ip_address"
        )

    @before_event(Insert)
    async def before_insert(self):
        # # Generate _id if not provided
        # if not self._id:
        #     self._id = str(uuid.uuid4())

        # Generate created_at if not provided
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc)

    @before_event(Replace)
    async def before_ubdate(self):
        # Generate updated_at if not provided
        if not self.updated_at:
            self.updated_at = datetime.now(timezone.utc)

    class Settings:
        name = "reviews"
        is_root = True
        max_nesting_depth = 1
        # max_nesting_depths_per_field = {}

    class Config:
        json_schema_extra = {
            "example": {
                "_id": str(PydanticObjectId(str(ObjectId()))),
                # "user_id": str(PydanticObjectId(str(ObjectId()))),
                # "product_id": str(PydanticObjectId(str(ObjectId()))),
                "rate_value": fake.random_int(min=0, max=10),
                "comment": fake.text(),
                "is_toxic_comment": fake.boolean(),
                "created_at": datetime.now(timezone.utc), # datetime.now(timezone.utc).replace(tzinfo=None) # fake.date_time_between(start_date='-1y', end_date='now')
                "updated_at": datetime.now(timezone.utc), # datetime.now(timezone.utc).replace(tzinfo=None) # fake.date_time_between(start_date='-1y', end_date='now')
                "ip_address": fake.ipv4()
            }
        }

__all__ = [
    "BaseReview"
]
