from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas import PostCreate
from ..crud import posts


async def create_post(db: AsyncSession, post: PostCreate):
    orders = [block.order for block in post.contents]

    if any(order < 1 for order in orders):
        raise ValueError("order у блоков должен быть положительным")

    if len(orders) != len(set(orders)):
        raise ValueError("order у блоков должен быть уникальным")
    
    return await posts.post_post(db, post)