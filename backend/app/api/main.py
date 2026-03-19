from fastapi import APIRouter

from .routes import posts

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(posts.router)
