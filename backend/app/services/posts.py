from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas import PostCreate, ContentBlockCreate
from ..crud import posts


async def create_post(db: AsyncSession, post: PostCreate):
    return await posts.post_post(db, post)

async def create_content_block(db: AsyncSession, block: ContentBlockCreate, post_id: int):
    post = await posts.get_post(db, post_id)
    if not post:
        raise ValueError("Пост не найден")
    
    last_order = post.content_blocks[-1].order if post.content_blocks else 0
    order = last_order + 1

    return await posts.post_content_block(db, block, post_id, order)