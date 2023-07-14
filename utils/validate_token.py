from typing import Annotated
from fastapi import Header
from utils.exceptions import Unauthorized
from utils.database import get_db


async def validate_token(x_token: Annotated[str, Header()]):
    database = await get_db()

    token_exists = await database.users.find_one({"token": x_token})
    print(token_exists)

    if not token_exists:
        raise Unauthorized("Invalid Token")
    else:
        print("Authorized")

    return True
