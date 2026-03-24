from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import main
from app.database import check_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await check_db()
    yield



app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Hello, World!"}

app.include_router(main.api_router)