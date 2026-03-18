from fastapi import APIRouter

from .schemas import PostCreate, ContentBlock

router = APIRouter(prefix="/posts")



@router.post("/")
def create_post(
    post: PostCreate
):
    return {"message": f"Post '{post.title}' created successfully!"}

@router.get("/{post_id}")
def get_post(post_id: int):
    return {"message": f"Post with ID {post_id} retrieved successfully!"}

@router.post("/{post_id}/content-blocks")
def create_content_block(post_id: int, content_block: ContentBlock):
    pass
    
    
