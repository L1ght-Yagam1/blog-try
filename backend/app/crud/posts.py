from typing import List

from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Post, ContentBlock
from ..schemas import ContentBlockCreate, PostCreate


async def get_posts(db: AsyncSession, offset: int, limit: int) -> list[Post]:
    posts_query = select(Post).offset(offset).limit(limit)

    result = await db.execute(posts_query)

    return list(result.scalars().all())

async def post_post(db: AsyncSession, new_post: PostCreate) -> Post:
    post = Post(title=new_post.title)
    
    for block in new_post.contents:
        post.content_blocks.append(
            ContentBlock(
                type=block.type,
                order=block.order,
                img_url=block.img_url,
                text=block.text
            )
        )

    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post


async def get_post(db: AsyncSession, post_id: int) -> Post:
    post_query = select(Post).where(Post.id == post_id).options(selectinload(Post.content_blocks))
    result = await db.execute(post_query)
    return result.scalars().first()

async def post_content_block(
        db: AsyncSession,
        block: ContentBlockCreate,
        post_id: int
):
    block_model = ContentBlock(
        type=block.type,
        post_id=post_id,
        order=block.order,
        img_url=block.img_url,
        text=block.text
    )
    db.add(block_model)
    await db.commit()
    await db.refresh(block_model)
    return block_model

# async def update_post(db: AsyncSession, post_id: int, title: str) -> Post:
#     post_query = update(Post).where(Post.id == post_id).values(title=title)
#     result = await db.execute(post_query)
#     post = result.scalar_one()
#     await db.commit()
#     return post.content_blocks



