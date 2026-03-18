from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes import router
from app.database import check_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    check_db()
    yield



app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Hello, World!"}




app.include_router(router)