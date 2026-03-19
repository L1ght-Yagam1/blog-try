from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .database import session_factory


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db)]
