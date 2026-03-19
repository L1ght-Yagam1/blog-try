from fastapi import APIRouter

from ...schemas import PostCreate, ContentBlock
from ...crud import posts
from ...deps import SessionDep

router = APIRouter(prefix="/posts")



@router.post("/")
async def create_post(
    db: SessionDep,
    post: PostCreate
):
    return await posts.post_post(db, post.title)


@router.get("/")
async def get_posts(
    db: SessionDep,
    skip: int = 0,
    limit: int = 3
):
    return await posts.get_posts(db, skip, limit)

@router.get("/{post_id}")
async def get_post(
    db: SessionDep,
    post_id: int
):
    return await posts.get_post(db, post_id)

@router.post("/{post_id}/content-blocks")
async def create_content_block(
    db: SessionDep,
    post_id: int,
    content_block: ContentBlock
):
    pass
    
    
