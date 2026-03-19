from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Post


async def get_posts(db: AsyncSession, offset: int, limit: int) -> list[Post]:
    posts_query = select(Post).offset(offset).limit(limit)

    result = await db.execute(posts_query)

    return list(result.scalars().all())

async def post_post(db: AsyncSession, title: str) -> Post:
    new_post = Post(title=title)
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post


async def get_post(db: AsyncSession, post_id: int) -> Post:
    post_query = select(Post).where(Post.id == post_id).options(selectinload(Post.content_blocks))
    result = await db.execute(post_query)
    return result.scalars().first()

# async def update_post(db: AsyncSession, post_id: int, title: str) -> Post:
#     post_query = update(Post).where(Post.id == post_id).values(title=title)
#     result = await db.execute(post_query)
#     post = result.scalar_one()
#     await db.commit()
#     return post.content_blocks



