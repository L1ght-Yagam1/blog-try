from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello, World!"}




app.include_router(router)