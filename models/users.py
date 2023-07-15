from pydantic import BaseModel

class CreateUsers(BaseModel):
    name: str
    lastname: str
    email: str