# Import required packages and modules
# from __future__ import annotations
# import logging as logging
# import sys as sys
# import os as os
# from decouple import config
# import asyncio as asyncio
# from typing import TYPE_CHECKING
from typing import TYPE_CHECKING, Optional, Any, Type, TypeVar, Generic, ForwardRef, Annotated, Union, List
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends, HTTPException, status, security
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from beanie import init_beanie
from app.configs.database import connect_to_database, close_database_connection, get_database
from app.errors.BadRequest import BadRequest
from app.errors.UnprocessableError import UnprocessableError
from app.utils.Logger import Logger
# import routes
from app.api.v1 import health_routes as health_routes
from app.api.v1 import user_routes as user_routes
# import models
from app.models.User import User as UserModel
from app.models.Review import Review as ReviewModel
from app.models.Product import Product as ProductModel
from app.models.Payment import Payment as PaymentModel
from app.models.OrderItem import OrderItem as OrderItemModel
from app.models.Order import Order as OrderModel
from app.models.Cart import Cart as CartModel
 
logging = Logger(__name__)

'''
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     logging.debug("startup has begun!!")
#     yield
#     logging.debug("shutdown has begun!!")
# app = FastAPI(lifespan=lifespan)
'''

app = FastAPI()

# Middlewares
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mounting static folder on serve for fetching static files
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

async def connect_and_init_db():
    try:
        await connect_to_database()
        db = await get_database()
        await init_beanie(
            database=db,
            document_models= [
                UserModel,
                ReviewModel,
                ProductModel,
                PaymentModel,
                OrderItemModel,
                OrderModel,
                CartModel
            ]
        )
        logging.debug("database initialized")
    except Exception as e:
        logging.exception("An error occurred while initializing the database", e)

# DB Events
app.add_event_handler("startup", connect_and_init_db)
app.add_event_handler("shutdown", close_database_connection)

# openapi schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Title",
        version="1.0.0",
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


# HTTP error responses
@app.exception_handler(BadRequest)
async def bad_request_handler(req: Request, exc: BadRequest) -> JSONResponse:
    return exc.gen_err_resp()


@app.exception_handler(RequestValidationError)
async def invalid_req_handler(
    req: Request,
    exc: RequestValidationError
) -> JSONResponse:
    logging.error(f"Request invalid. {str(exc)}")
    return JSONResponse(
        status_code=400,
        content={
            "type": "about:blank",
            "title": "Bad Request",
            "status": 400,
            "detail": [str(exc)]
        }
    )


@app.exception_handler(UnprocessableError)
async def unprocessable_error_handler(
    req: Request,
    exc: UnprocessableError
) -> JSONResponse:
    return exc.gen_err_resp()


# # API Path
# # # Health
app.include_router(
    health_routes.router,
    prefix="/v1",
    tags=["health"]
)

# # # User
app.include_router(
    user_routes.router,
    prefix="/v1",
    tags=["user"]
)


__all__ = [
    "app"
]

