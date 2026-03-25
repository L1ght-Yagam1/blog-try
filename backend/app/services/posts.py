from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas import PostCreate, ContentBlockCreate
from ..crud import posts
from ..enums import ContentBlockType

@dataclass
class ContentBlockService:
    type: ContentBlockType
    order: int
    text: str | None
    img_url: str | None




async def create_post(db: AsyncSession, post_in: PostCreate):
    blocks = [ContentBlockService(
        type=block.type,
        order=index,
        text=block.text,
        img_url=block.img_url
    ) for index, block in enumerate(post_in.contents, start=1)]


    return await posts.post_post(db, post_in.title, blocks)

async def create_content_block(db: AsyncSession, block: ContentBlockCreate, post_id: int):
    post = await posts.get_post(db, post_id)
    if not post:
        raise ValueError("Пост не найден")
    
    last_order = post.content_blocks[-1].order if post.content_blocks else 0
    order = last_order + 1

    return await posts.post_content_block(db, block, post_id, order)