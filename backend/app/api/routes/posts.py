from fastapi import APIRouter

from ...schemas import PostCreate, ContentBlockCreate, PostPublic, ContentBlockPublic
from ...services import posts as post_service
from ...crud import posts
from ...deps import SessionDep

router = APIRouter(prefix="/posts", tags=["posts"])



@router.post("/", response_model=PostPublic, response_model_exclude_none=True)
async def create_post(
    db: SessionDep,
    post: PostCreate
):
    return await post_service.create_post(db, post)


@router.get("/", response_model=list[PostPublic], response_model_exclude_none=True)
async def get_posts(
    db: SessionDep,
    skip: int = 0,
    limit: int = 3
):
    return await posts.get_posts(db, skip, limit)

@router.get("/{post_id}", response_model=PostPublic, response_model_exclude_none=True)
async def get_post(
    db: SessionDep,
    post_id: int
):
    return await posts.get_post(db, post_id)

@router.post("/{post_id}/content-blocks", response_model=ContentBlockPublic, response_model_exclude_none=True)
async def create_content_block(
    db: SessionDep,
    post_id: int,
    content_block: ContentBlockCreate
):
    return await post_service.create_content_block(db, content_block, post_id)
    
    
