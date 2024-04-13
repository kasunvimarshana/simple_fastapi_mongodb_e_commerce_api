# Import required packages and modules
# from __future__ import annotations
# import logging as logging
# import sys as sys
# import os as os
from decouple import config
# import asyncio as asyncio
# from typing import TYPE_CHECKING

class Setting:
    # pass
    def __init__(self):
        ## database
        self.DB_USER = config("DB_USER", default=None)
        self.DB_PASSWORD = config("DB_PASSWORD", default=None)
        self.DB_HOST = config("DB_HOST", default=None)
        self.DB_PORT = config("DB_PORT", default=None)
        self.DB_NAME = config("DB_NAME", default=None)
        self.DB_MAX_CONN_COUNT = int(config("DB_MAX_CONN_COUNT", default=0))
        self.DB_MIN_CONN_COUNT = int(config("DB_MIN_CONN_COUNT", default=0))
        self.DB_UUID_REPRESENTATION = config("DB_UUID_REPRESENTATION", "standard")
        ## JWT
        ## openssl rand -hex 32
        self.TOKEN_SECRET_KEY = config("TOKEN_SECRET_KEY", default=None)
        self.TOKEN_ALGORITHM = config("TOKEN_ALGORITHM", default="HS256")
        self.TOKEN_EXPIRE_MINUTES = int(config("TOKEN_EXPIRE_MINUTES", default=(1440 * 365 * 10)))

__all__ = [
    "Setting"
]
