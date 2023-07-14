import secrets
from bson import ObjectId
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorDatabase
from utils.exceptions import DuplicateRecord, NotFoundRecord


from models.users import CreateUsers
from utils.database import get_db



router = APIRouter(
    prefix="/users",
    tags=["users"],
)
 
@router.post("")
async def create_users(
    create_user: CreateUsers, 
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):

    user_exists = await database.users.find_one({
        "email": create_user.email
    })
    if user_exists:
        raise DuplicateRecord(f"User {create_user.email} already exists")
    print(database)

    inserted_id = await database.users.insert_one({
        "_id":str(ObjectId()),
        "name": create_user.name,
        "lastname": create_user.lastname,
        "email": create_user.email,
        "token":secrets.token_hex(12),
      
    })
    return {"created_users": inserted_id.inserted_id} 

@router.post("/{user_id}")
async def get_users(
    users_id:str,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    user = await database.users.find_one(
        {
            "_id": users_id,
        }
    )

    if not user:
        raise NotFoundRecord(f"User with id {users_id} does not exists")
    return user

