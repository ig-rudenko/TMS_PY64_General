from fastapi import FastAPI

from src.handlers.posts import router as posts_router

app = FastAPI(
    description="Posts API",

)

app.include_router(posts_router, prefix="/api/v1")
