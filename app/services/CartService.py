# Import required packages and modules
# from __future__ import annotations
# import logging as logging
# import sys as sys
import os as os
# import platform as platform
# import psutil as psutil
# from decouple import config
# import asyncio as asyncio 
from typing import TYPE_CHECKING, \
    Optional, \
    Any, \
    Union, \
    Type, \
    TypeVar, \
    Generic, \
    ForwardRef, \
    Annotated, \
    List
from fastapi import FastAPI, APIRouter, Request, Depends, HTTPException, status, Body, Query
import pymongo as pymongo
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from beanie import PydanticObjectId, MergeStrategy
from beanie import operators as operators
from datetime import datetime, timezone
import app.configs.database as database
from app.configs.Setting import Setting as Setting
from app.utils.Logger import Logger as Logger
# import models
from app.models.Cart import Cart as CartModel
from app.models.User import User as UserModel
from app.models.Product import Product as ProductModel
# import schemas
from app.schemas.User import User as UserSchema
from app.schemas.Cart import Cart as CartSchema
from app.schemas.CartItemCreateRequest import CartItemCreateRequest as CartItemCreateRequestSchema
from app.schemas.CartItemUpdateRequest import CartItemUpdateRequest as CartItemUpdateRequestSchema
from app.schemas.CartReadRequest import CartReadRequest as CartReadRequestSchema
from app.schemas.PaginateResponse import PaginateResponse as PaginateResponseSchema

class CartService:
    def __init__(self):
        self.settings = Setting()
        self.logger = Logger(__name__)


    async def create_cart_item(
            self, 
            cart_item_create_request_schema: CartItemCreateRequestSchema, 
            db: AsyncIOMotorDatabase, 
            current_user: Optional[Union[UserSchema, None]], 
            client_ip: Optional[Union[str, None]]
        ) -> Optional[CartSchema]:
            self.logger.debug("create_cart_item called")
            async with await db.client.start_session() as session:
                try:
                    async with session.start_transaction():
                        cart_item_create_request_schema_dict = cart_item_create_request_schema.model_dump(
                            exclude_unset=True,
                            # exclude_none=True
                        )
                        created_at = datetime.now(tz=timezone.utc)
                        cart_item_create_request_schema_dict["created_at"] = created_at
                        cart_item_create_request_schema_dict["ip_address"] = client_ip
                        if current_user is not None:
                             user_instance = await UserModel.find_one(UserModel.id == PydanticObjectId(current_user.id))
                             cart_item_create_request_schema_dict["user"] = user_instance
                        if "product_id" in cart_item_create_request_schema_dict and cart_item_create_request_schema_dict.get("product_id") is not None:
                            product_id = cart_item_create_request_schema_dict.get("product_id")
                            product_instance = await ProductModel.find_one(ProductModel.id == PydanticObjectId(product_id))
                            cart_item_create_request_schema_dict["product"] = product_instance
                        
                        cart_instance = CartModel(
                            **cart_item_create_request_schema_dict
                        )

                        # cart_instance = await CartModel.insert_one(cart_instance, session=session)
                        cart_instance = await cart_instance.create(session=session)

                    # Commit transaction if everything succeeds
                    await session.commit_transaction()
                    return CartSchema.model_validate(cart_instance.model_dump(by_alias=True))
                except Exception as e:
                    # Rollback transaction if an error occurs
                    if not session.has_ended and session.in_transaction:
                        await session.abort_transaction()
                    self.logger.exception("Error in create_cart_item", e)
                    raise e

    async def update_cart_item(
            self, 
            id: str,
            cart_item_update_request_schema: CartItemUpdateRequestSchema, 
            db: AsyncIOMotorDatabase, 
            current_user: Optional[Union[UserSchema, None]], 
            client_ip: Optional[Union[str, None]]
        ) -> Optional[CartSchema]:
            self.logger.debug("update_cart_item called")
            async with await db.client.start_session() as session:
                try:
                    async with session.start_transaction():
                        cart_instance = await CartModel.find_one(CartModel.id == PydanticObjectId(id))
                        if not cart_instance:
                            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart Item not found")

                        cart_item_update_request_schema_dict = cart_item_update_request_schema.model_dump(
                            exclude_unset=True,
                            # exclude_none=True
                        )
                        updated_at = datetime.now(tz=timezone.utc)
                        cart_item_update_request_schema_dict["updated_at"] = updated_at
                        if current_user is not None:
                             user_instance = await UserModel.find_one(UserModel.id == PydanticObjectId(current_user.id))
                             cart_item_update_request_schema_dict["user"] = user_instance
                        if "product_id" in cart_item_update_request_schema_dict and cart_item_update_request_schema_dict.get("product_id") is not None:
                            product_id = cart_item_update_request_schema_dict.get("product_id")
                            product_instance = await ProductModel.find_one(ProductModel.id == PydanticObjectId(product_id))
                            cart_item_update_request_schema_dict["product"] = product_instance

                        await cart_instance.update({"$set": cart_item_update_request_schema_dict}, session=session)
                    # Commit transaction if everything succeeds
                    await session.commit_transaction()

                    return CartSchema.model_validate(cart_instance.model_dump(by_alias=True))
                except Exception as e:
                    # Rollback transaction if an error occurs
                    if not session.has_ended and session.in_transaction:
                        await session.abort_transaction()
                    self.logger.exception("Error in update_cart_item", e)
                    raise e

    async def delete_cart_item(
            self, 
            id: str,
            db: AsyncIOMotorDatabase, 
            current_user: Optional[Union[UserSchema, None]], 
            client_ip: Optional[Union[str, None]]
        ) -> None:
            self.logger.debug("delete_cart_item called")
            async with await db.client.start_session() as session:
                try:
                    async with session.start_transaction():
                        cart_instance = await CartModel.find_one(CartModel.id == PydanticObjectId(id))
                        if not cart_instance:
                            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart Item not found")
                        await cart_instance.delete(
                                # link_rule=DeleteRules.DELETE_LINKS, 
                                session=session
                            )
                    # Commit transaction if everything succeeds
                    await session.commit_transaction()

                except Exception as e:
                    # Rollback transaction if an error occurs
                    if not session.has_ended and session.in_transaction:
                        await session.abort_transaction()
                    self.logger.exception("Error in delete_cart_item", e)
                    raise e


    async def read_cart_item_by_id(
            self, 
            id: str,
            db: AsyncIOMotorDatabase, 
            current_user: Optional[Union[UserSchema, None]], 
            client_ip: Optional[Union[str, None]]
        ) -> Optional[CartSchema]:
            self.logger.debug("read_cart_item_by_id called")
            try:
                cart_instance = await CartModel.find_one(operators.Eq(CartModel.id, PydanticObjectId(id)), fetch_links=True)
                if not cart_instance:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart Item not found")

                return CartSchema.model_validate(cart_instance.model_dump(by_alias=True))
            except Exception as e:
                self.logger.exception("Error in read_cart_item_by_id", e)
                raise e

    async def read_cart(
            self, 
            cart_read_request_schema: CartReadRequestSchema, 
            db: AsyncIOMotorDatabase, 
            current_user: Optional[Union[UserSchema, None]], 
            client_ip: Optional[Union[str, None]]
        ) -> Optional[PaginateResponseSchema[List[CartSchema]]]:
            self.logger.debug("read_cart called")
            try:
                query = CartModel.find(fetch_links=True)
                cart_read_request_schema_dict = cart_read_request_schema.model_dump(
                            exclude_unset=True,
                            # exclude_none=True
                        )
                
                # Filter by user.id if provided
                if current_user is not None:
                    query = query.find(ProductModel.user.id == PydanticObjectId(current_user.id))

                total_count = await query.count()

                if "paginate" in cart_read_request_schema_dict and cart_read_request_schema_dict.get("paginate") == True:
                    query.skip(
                            cart_read_request_schema_dict.get("skip", 0)
                        ).limit(
                            cart_read_request_schema_dict.get("limit", 0)
                        )
                
                results = await query.to_list(
                        # length=cart_read_request_schema_dict.get("limit", 0)
                    )

                product_schema_list = [CartSchema.model_validate(v.model_dump(by_alias=True)) for v in results]
                return PaginateResponseSchema[List[CartSchema]](count=total_count, result=product_schema_list)

            except Exception as e:
                self.logger.exception("Error in read_reviews", e)
                raise e


    async def delete_cart(
            self, 
            db: AsyncIOMotorDatabase, 
            current_user: Optional[Union[UserSchema, None]], 
            client_ip: Optional[Union[str, None]]
        ) -> None:
            self.logger.debug("delete_cart called")
            async with await db.client.start_session() as session:
                try:
                    async with session.start_transaction():
                        query = CartModel.find(fetch_links=False)

                        # Filter by user.id if provided
                        if current_user is not None:
                            query = query.find(ProductModel.user.id == PydanticObjectId(current_user.id))
                        
                        await query.delete(
                            # link_rule=DeleteRules.DELETE_LINKS, 
                            session=session
                        )

                    # Commit transaction if everything succeeds
                    await session.commit_transaction()

                except Exception as e:
                    # Rollback transaction if an error occurs
                    if not session.has_ended and session.in_transaction:
                        await session.abort_transaction()
                    self.logger.exception("Error in delete_cart", e)
                    raise e
                

__all__ = [
    "CartService"
]
