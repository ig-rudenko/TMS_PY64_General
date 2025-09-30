from fastapi import FastAPI

from src.api.handlers.posts import router as posts_router
from src.api.handlers.auth import router as auth_router

from src.database.connector import db_connector
from src.settings import settings

db_connector.init(settings.database_url)

app = FastAPI(description="Posts API")

app.include_router(posts_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
