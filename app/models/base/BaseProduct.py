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

class BaseProduct(Document):
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
    sku: Optional[str] = Field(
            default=None, 
            description="sku"
        ) # Indexed(str, unique=True)
    name: Optional[str] = Field(
            default=None, 
            description="name"
        )
    qty_in_stock: Optional[int] = Field(
            default=0, 
            description="qty_in_stock"
        )
    price: Optional[Decimal] = Field(
            default=Decimal(0.0), 
            description="price"
        ) # Optional[float]
    image: Optional[str] = Field(
            default=None, 
            description="image"
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
    # ip_address: Optional[str] = Field(
    #         default=None, 
    #         description="ip_address"
    #     )
    remark: Optional[str] = Field(
            default=None, 
            description="remark"
        )

    def _generate_sku(self):
        # sku = self.name.replace(" ", "_").lower() + "_" + str(uuid.uuid4().hex)[:6]
        sku = str(uuid4())
        return sku

    @before_event(Insert)
    async def before_insert(self):
        # # Generate _id if not provided
        # if not self._id:
        #     self._id = str(uuid.uuid4())

        # Generate sku if not provided
        if not self.sku:
            self.sku = self._generate_sku()

        # Generate created_at if not provided
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc)

    @before_event(Replace)
    async def before_ubdate(self):
        # Generate updated_at if not provided
        if not self.updated_at:
            self.updated_at = datetime.now(timezone.utc)

    class Settings:
        name = "products"
        is_root = True
        max_nesting_depth = 1
        # max_nesting_depths_per_field = {}

    class Config:
        json_schema_extra = {
            "example": {
                "_id": str(PydanticObjectId(str(ObjectId()))),
                "sku": str(fake.uuid4()), # fake.uuid4().hex[:12],
                "name": fake.word(),
                "qty_in_stock": fake.random_int(min=0, max=100),
                "price": Decimal(fake.pydecimal(min_value=10, max_value=1000, right_digits=2)),
                "image": fake.image_url(),
                "created_at": datetime.now(timezone.utc), # datetime.now(timezone.utc).replace(tzinfo=None) # fake.date_time_between(start_date='-1y', end_date='now')
                "updated_at": datetime.now(timezone.utc), # datetime.now(timezone.utc).replace(tzinfo=None) # fake.date_time_between(start_date='-1y', end_date='now')
                "ip_address": fake.ipv4(),
                "remark": fake.text()
            }
        }

__all__ = [
    "BaseProduct"
]
