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
from app.models.base.BasePayment import BasePayment
from app.models.base.BaseOrder import BaseOrder

fake = Faker()

class Payment(BasePayment):
    # pass
    order: Optional[Link[BaseOrder]] = Field(
            default=None, 
            alias="order",
            description="order"
        )


__all__ = [
    "Payment"
]
