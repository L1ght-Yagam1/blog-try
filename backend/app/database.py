from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from .settings import get_async_database_url


engine: AsyncEngine = create_async_engine(
    get_async_database_url(),
    pool_pre_ping=True,
)
session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


async def check_db() -> None:
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ DB connection OK")
    except Exception as e:
        print("❌ DB connection FAILED:", e)
