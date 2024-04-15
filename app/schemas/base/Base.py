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
    List, \
    Dict
from pydantic import BaseModel, Field, ValidationError, GetJsonSchemaHandler, condecimal
from pydantic.json import pydantic_encoder
from pydantic_core import CoreSchema
from datetime import datetime, timezone, timedelta
# from decimal import Decimal

class Base(BaseModel):
    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> Dict[str, Any]:
        json_schema = super().__get_pydantic_json_schema__(core_schema, handler)
        json_schema = handler.resolve_ref_schema(json_schema)
        json_schema.update(examples='examples')
        return json_schema

# Base.model_rebuild()

if __name__ == "__main__":
    print(Base.model_json_schema())
    """
    {'examples': 'examples', 'properties': {}, 'title': 'Model', 'type': 'object'}
    """

__all__ = [
    "Base"
]
