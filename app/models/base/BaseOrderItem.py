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

class BaseOrderItem(Document):
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
    # order_id: Optional[PydanticObjectId] = Field(
    #         default=None, 
    #         description="order_id"
    #     )
    # product_id: Optional[PydanticObjectId] = Field(
    #         default=None, 
    #         description="product_id"
    #     )
    qty: Optional[int] = Field(
            default=0, 
            description="qty"
        )
    price: Optional[Decimal] = Field(
            default=Decimal(0.0), 
            description="price"
        ) # Optional[float]

    class Settings:
        name = "order_items"
        is_root = True
        max_nesting_depth = 1
        # max_nesting_depths_per_field = {}

    class Config:
        json_schema_extra = {
            "example": {
                "_id": str(PydanticObjectId(str(ObjectId()))),
                # "order_id": str(PydanticObjectId(str(ObjectId()))),
                # "product_id": str(PydanticObjectId(str(ObjectId()))),
                "qty": fake.random_int(min=1, max=100),
                "price": Decimal(fake.pydecimal(min_value=10, max_value=1000, right_digits=2))
            }
        }

__all__ = [
    "BaseOrderItem"
]