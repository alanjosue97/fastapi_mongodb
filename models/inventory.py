from typing import Optional
from pydantic import BaseModel


class CreateInventory(BaseModel):
    _id: str
    equipment:str
    brand:str
    model:str
    serialnumber:str
    price:float
    
class GetInventory(BaseModel):
    _id: str
    equipment:str
    brand:str
    model:str
    serialnumber:str
    price:float