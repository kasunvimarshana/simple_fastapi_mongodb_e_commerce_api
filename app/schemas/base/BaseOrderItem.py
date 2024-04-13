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
from decimal import Decimal
from faker import Faker

fake = Faker()

class BaseOrderItem(BaseModel):
    _id: Optional[str] = Field(
            default=None,
            description="_id"
        )
    # order_id: Optional[str] = Field(
    #         default=None, 
    #         description="order_id"
    #     )
    # product_id: Optional[str] = Field(
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
        ) # Optional[condecimal(decimal_places=2, max_digits=10)] # Optional[float]


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
                # "order_id": str(fake.uuid4()),
                # "product_id": str(fake.uuid4()),
                "qty": fake.random_int(min=1, max=100),
                "price": Decimal(fake.pydecimal(min_value=10, max_value=1000, right_digits=2))
            }
        }

# BaseOrderItem.model_rebuild()

__all__ = [
    "BaseOrderItem"
]
