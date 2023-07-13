from fastapi import FastAPI
from routers import inventory 


app = FastAPI()

app.include_router(inventory.router)

@app.get("/home", tags=["Home"])
async def home():
    return{
        "message": "Home page"
    }