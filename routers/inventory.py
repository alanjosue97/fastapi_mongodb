from bson import ObjectId
from typing import Annotated
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi.responses import JSONResponse

from models.inventory import CreateInventory, GetInventory
from utils.database import get_db
from utils.validate_token import validate_token
from utils.exceptions import NotFoundRecord


router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)

@router.get("", dependencies=[Depends(validate_token)])
async def list_inventory(database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    inventory_list = [inventory async for inventory in database.inventory.find({})]
    
    return JSONResponse(
        content=jsonable_encoder(inventory_list),
        status_code=200
    )
     


@router.post("",dependencies=[Depends(validate_token)])
async def create_inventory(create_inventory: CreateInventory, database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):

    
    print(database)

    inserted_id = await database.inventory.insert_one({
        "_id":str(ObjectId()),
        "equipment": create_inventory.equipment,
        "brand": create_inventory.brand,
        "model": create_inventory.model,
        "serialnumber": create_inventory.serialnumber,
        "price": create_inventory.price 
    })

    return JSONResponse(
        content= {"Created_Inventory": inserted_id.inserted_id},
        status_code=201

    )



@router.post("/{inventory_id}")
async def get_inventory(
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
    inventory_id:str,
):
    inventoy = await database.inventory.find_one(
        {
            "_id": inventory_id,
        }
    )
    if not inventoy:
        raise NotFoundRecord(f"Inventory with id {inventory_id} does no exists")

    return JSONResponse(
        content=inventoy,
        status_code=200
    )