from fastapi import FastAPI

from src.handlers.posts import router as posts_router
from src.handlers.auth import router as auth_router

app = FastAPI(description="Posts API")

app.include_router(posts_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
