from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie


from api.api_v1.router import router
from core.config import settings
from models.todo_model import Todo
from models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """
    
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).fodoist
    
    await init_beanie(
        database=db_client,
        document_models= [
           User,
           Todo
        ]
    )

app.include_router(router, prefix=settings.API_V1_STR)