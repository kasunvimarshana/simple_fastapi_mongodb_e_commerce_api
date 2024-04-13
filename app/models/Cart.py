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
from app.models.base.BaseCart import BaseCart
from app.models.base.BaseProduct import BaseProduct
from app.models.base.BaseUser import BaseUser

fake = Faker()

class Cart(BaseCart):
    # pass
    product: Optional[Link[BaseProduct]] = Field(
            default=None, 
            description="product"
        )
    user: Optional[Link[BaseUser]] = Field(
            default=None, 
            description="user"
        )

    class Config(BaseCart.Config):
        base_cart_schema = BaseCart.Config.json_schema_extra["example"]
        base_product_schema = BaseProduct.Config.json_schema_extra["example"]
        base_user_schema = BaseUser.Config.json_schema_extra["example"]
        '''
        # populate_by_name = True
        # json_encoders = {
        #     BackLink: lambda x: None,  # Exclude BackLink fields from serialization
        # }
        '''
        json_schema_extra = {
            "example": {
                **base_cart_schema,
                "product": {
                    **base_product_schema
                },
                "user": {
                    **base_user_schema
                }
            }
        }

__all__ = [
    "Cart"
]