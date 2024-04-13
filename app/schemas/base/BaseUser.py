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
    TypeVar, \
    ForwardRef, \
    Annotated, \
    Union, \
    List
from pydantic import BaseModel, Field, ValidationError, condecimal
from pydantic.json import pydantic_encoder
from datetime import datetime, timezone, timedelta
# from decimal import Decimal
from faker import Faker
from app.enums.UserRole import UserRole as UserRole

fake = Faker()

class BaseUser(BaseModel):
    _id: Optional[str] = Field(
            default=None,
            description="_id"
        )
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
        )
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
            default=None, 
            description="created_at"
        )
    updated_at: Optional[datetime] = Field(
            default=None, 
            description="updated_at"
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

    class Config:
        # pass
        # populate_by_name = True
        allow_population_by_field_name = True
        json_encoders = {
            # CustomType: lambda v: pydantic_encoder(v) if isinstance(v, CustomType) else None,
            # datetime: lambda v: v.isoformat() if isinstance(v, datetime) else None,
            # BackLink: lambda x: None,  # Exclude BackLink fields from serialization
        }
        json_schema_extra = {
            "example": {
                "_id": str(fake.uuid4()),
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

# BaseUser.model_rebuild()

__all__ = [
    "BaseUser"
]
