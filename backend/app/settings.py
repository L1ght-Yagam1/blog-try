from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.engine import make_url

BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"{name} is not set")

    return value


def _with_driver(database_url: str, drivername: str) -> str:
    parsed_url = make_url(database_url)

    if parsed_url.get_backend_name() != "postgresql":
        return database_url

    return parsed_url.set(drivername=drivername).render_as_string(
        hide_password=False
    )


def get_async_database_url() -> str:
    explicit_url = os.getenv("ASYNC_DATABASE_URL")
    if explicit_url:
        return explicit_url

    return _with_driver(_require_env("DATABASE_URL"), "postgresql+asyncpg")


def get_sync_database_url() -> str:
    explicit_url = os.getenv("SYNC_DATABASE_URL")
    if explicit_url:
        return explicit_url

    return _with_driver(_require_env("DATABASE_URL"), "postgresql+psycopg2")
