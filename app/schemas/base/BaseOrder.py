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
from app.enums.OrderStatus import OrderStatus as OrderStatus

fake = Faker()

class BaseOrder(BaseModel):
    _id: Optional[str] = Field(
            default=None,
            description="_id"
        )
    # user_id: Optional[str] = Field(
    #         default=None, 
    #         description="user_id"
    #     )
    created_at: Optional[datetime] = Field(
            default=None, 
            description="created_at"
        )
    updated_at: Optional[datetime] = Field(
            default=None, 
            description="updated_at"
        )
    ip_address: Optional[str] = Field(
            default=None, 
            description="ip_address"
        )
    order_total_amount: Optional[Decimal] = Field(
            default=Decimal(0.0), 
            description="order_total_amount"
        ) # Optional[condecimal(decimal_places=2, max_digits=10)] # Optional[float]
    order_due_amount: Optional[Decimal] = Field(
            default=Decimal(0.0), 
            description="order_due_amount"
        ) # Optional[condecimal(decimal_places=2, max_digits=10)] # Optional[float]
    order_status: Optional[OrderStatus] = Field(
            default=None, 
            description="order_status"
        )
    remark: Optional[str] = Field(
            default=None, 
            description="remark"
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
                # "user_id": str(fake.uuid4()),
                "created_at": datetime.now(timezone.utc), # datetime.now(timezone.utc).replace(tzinfo=None) # fake.date_time_between(start_date='-1y', end_date='now')
                "updated_at": datetime.now(timezone.utc), # datetime.now(timezone.utc).replace(tzinfo=None) # fake.date_time_between(start_date='-1y', end_date='now')
                "ip_address": fake.ipv4(),
                "order_total_amount": Decimal(fake.pydecimal(min_value=10, max_value=1000, right_digits=2)),
                "order_due_amount": Decimal(fake.pydecimal(min_value=0, max_value=1000, right_digits=2)),
                "order_status": fake.random_element(elements=[status.value for status in OrderStatus]),
                "remark": fake.text()
            }
        }

# BaseOrder.model_rebuild()

__all__ = [
    "BaseOrder"
]
