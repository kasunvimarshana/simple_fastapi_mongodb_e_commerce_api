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
from app.enums.UserRole import UserRole as UserRole

fake = Faker()

class BaseUser(Document):
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
    first_name: Optional[str] = Field(
            default=None, 
            description="first_name"
        )
    last_name: Optional[str] = Field(
            default=None, 
            description="last_name"
        )
    email: Optional[str] = Field(
            default=None, 
            description="email"
        ) # Indexed(str, unique=True)
    password: Optional[str] = Field(
            default=None, 
            description="password"
        )
    phone_number: Optional[str] = Field(
            default=None, 
            description="phone_number"
        )
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
    user_role: Optional[UserRole] = Field(
            default=None, 
            description="user_role"
        )
    latitude: Optional[float] = Field(
            default=None, 
            description="latitude"
        ) # coordinate that specifies the north–south position of a point on the surface of the Earth or another celestial body. Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator
    longitude: Optional[float] = Field(
            default=None, 
            description="longitude"
        ) # geographic coordinate that specifies the east–west position of a point on the surface of the Earth, or another celestial body. It is an angular measurement, usually expressed in degrees and denoted by the Greek letter lambda
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
        name = "users"
        is_root = True
        max_nesting_depth = 1
        # max_nesting_depths_per_field = {}

    class Config:
        json_schema_extra = {
            "example": {
                "_id": str(PydanticObjectId(str(ObjectId()))),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "password": fake.password(),
                "phone_number": fake.phone_number(),
                "image": fake.image_url(),
                "created_at": datetime.now(timezone.utc), # datetime.now(timezone.utc).replace(tzinfo=None) # fake.date_time_between(start_date='-1y', end_date='now')
                "updated_at": datetime.now(timezone.utc), # datetime.now(timezone.utc).replace(tzinfo=None) # fake.date_time_between(start_date='-1y', end_date='now')
                "user_role": fake.random_element(elements=[role.value for role in UserRole]),
                "latitude": fake.latitude(),
                "longitude": fake.longitude(),
                "ip_address": fake.ipv4()
            }
        }

__all__ = [
    "BaseUser"
]

