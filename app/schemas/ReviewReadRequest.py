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
from pydantic import BaseModel, \
    dataclasses, \
    ConfigDict, \
    ValidationError, \
    ValidationInfo, \
    validator, \
    field_validator, \
    field_serializer, \
    model_serializer, \
    Field, \
    AliasChoices, \
    condecimal, \
    GetJsonSchemaHandler
from pydantic.json import pydantic_encoder
from beanie import PydanticObjectId, BackLink
# from datetime import datetime, timezone, timedelta
# from decimal import Decimal
from faker import Faker
from .PaginateRequest import PaginateRequest

fake = Faker()

class ReviewReadRequest(PaginateRequest):
    rate_value: Optional[float] = Field(
            default=0, 
            alias="rate_value",
            description="rate_value"
        )
    is_toxic_comment: Optional[bool] = Field(
            default=False, 
            alias="is_toxic_comment",
            description="is_toxic_comment"
        )
    user_id: Optional[str] = Field(
            default=None, 
            alias="user_id",
            description="user_id"
        )
    product_id: Optional[str] = Field(
            default=None, 
            alias="product_id",
            description="product_id"
        )
    

    class Config:
        # pass
        paginate_request_schema = PaginateRequest.Config.json_schema_extra["example"]
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
                **paginate_request_schema,
                "rate_value": fake.random_int(min=0, max=10),
                "is_toxic_comment": fake.boolean(),
                "user_id": str(fake.uuid4()),
                "product_id": str(fake.uuid4()),
            }
        }

# ReviewReadRequest.model_rebuild()

__all__ = [
    "ReviewReadRequest"
]
