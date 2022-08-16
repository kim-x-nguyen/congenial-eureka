from fastapi import APIRouter, Query
from src.models.user import UserModel
from typing import Optional

# APIRouter creates path operations for user model
route = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={
        404: {"description": "Not found"}
    })

@route.get("/")
async def get_root():
    return {"message": "Hello World"}


@route.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "first_name": "John", "last_name": "Doe", "email": "test@test.com", "age": 30}

@route.post("/")
async def create_user(user: UserModel):
    return {"user_id": user.user_id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email, "age": user.age}

@route.put("/{user_id}")
async def update_user(user_id: int, user: UserModel):
    return {"user_id": user_id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email, "age": user.age}

@route.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"user_id": user_id}

