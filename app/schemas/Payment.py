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
from app.schemas.base.BasePayment import BasePayment
from app.schemas.base.BaseOrder import BaseOrder

fake = Faker()

class Payment(BasePayment):
    # pass
    order: Optional[Union[BaseOrder, dict]] = Field(
            default=None, 
            description="order"
        )
    

    class Config(BasePayment.Config):
        # pass
        base_payment_schema = BasePayment.Config.json_schema_extra["example"]
        base_order_schema = BaseOrder.Config.json_schema_extra["example"]
        # populate_by_name = True
        allow_population_by_field_name = True
        json_encoders = {
            # CustomType: lambda v: pydantic_encoder(v) if isinstance(v, CustomType) else None,
            # datetime: lambda v: v.isoformat() if isinstance(v, datetime) else None,
            # BackLink: lambda x: None,  # Exclude BackLink fields from serialization
        }
        json_schema_extra = {
            "example": {
                **base_payment_schema,
                "order": {
                    **base_order_schema
                }
            }
        }

# Payment.model_rebuild()

__all__ = [
    "Payment"
]
