# Import required packages and modules
# from __future__ import annotations
# import logging as logging
# import sys as sys
# import os as os
from decouple import config
from typing import TYPE_CHECKING, \
    Optional, \
    Any
from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    # pass
    PROJECT_NAME: Optional[str] = config(
        "PROJECT_NAME", 
        default=None, 
        cast=str
    )
	
	# model_config = SettingsConfigDict(env_file=".env")

    class Config:
        # pass
        case_sensitive = True

if __name__ == "__main__":
    print(Setting().model_dump())

__all__ = [
    "Setting"
]
