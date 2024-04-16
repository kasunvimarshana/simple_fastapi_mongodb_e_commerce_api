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
from pydantic import BaseModel, Field, ValidationError, AliasChoices, condecimal
from pydantic.json import pydantic_encoder
from beanie import PydanticObjectId, BackLink
from datetime import datetime, timezone, timedelta
# from decimal import Decimal
from faker import Faker
from uuid import UUID, uuid4

fake = Faker()

class HealthResource(BaseModel):
    # pass
    system: Optional[Any] = Field(
            default=None, 
            alias="system",
            description="system"
        )
    processor: Optional[Any] = Field(
            default=None, 
            alias="processor",
            description="processor"
        )
    architecture: Optional[Any] = Field(
            default=None, 
            alias="architecture",
            description="architecture"
        )
    memory: Optional[Any] = Field(
            default=None, 
            alias="memory",
            description="memory"
        )
    disk: Optional[Any] = Field(
            default=None, 
            alias="disk",
            description="disk"
        )
    database: Optional[Any] = Field(
            default=None, 
            alias="database",
            description="database"
        )

    class Config:
        # pass
        populate_by_name = True
        arbitrary_types_allowed = True # required for the _id
        use_enum_values = True
        # json_encoders = {
        #     # CustomType: lambda v: pydantic_encoder(v) if isinstance(v, CustomType) else None,
        #     # datetime: lambda v: v.isoformat() if isinstance(v, datetime) else None,
        #     # BackLink: lambda x: None,  # Exclude BackLink fields from serialization
        # }
        json_schema_extra = {
            "example": {
                
            }
        }


# HealthResource.model_rebuild()

__all__ = [
    "HealthResource"
]