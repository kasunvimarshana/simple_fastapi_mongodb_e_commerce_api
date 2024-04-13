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
from app.schemas.base.BaseProduct import BaseProduct
from app.schemas.base.BaseReview import BaseReview

fake = Faker()

class Product(BaseProduct):
    # pass
    reviews: Optional[List[Union[BaseReview, dict]]] = Field(
            default=None, 
            description="reviews", 
            original_field="product"
        )
    

    class Config(BaseProduct.Config):
        # pass
        base_product_schema = BaseProduct.Config.json_schema_extra["example"]
        base_review_schema = BaseReview.Config.json_schema_extra["example"]
        # populate_by_name = True
        allow_population_by_field_name = True
        json_encoders = {
            # CustomType: lambda v: pydantic_encoder(v) if isinstance(v, CustomType) else None,
            # datetime: lambda v: v.isoformat() if isinstance(v, datetime) else None,
            # BackLink: lambda x: None,  # Exclude BackLink fields from serialization
        }
        json_schema_extra = {
            "example": {
                **base_product_schema,
                "reviews": [
                    {
                        **base_review_schema
                    }
                ]
            }
        }

# Product.model_rebuild()

__all__ = [
    "Product"
]