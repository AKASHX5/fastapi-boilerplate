from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from app.core.config import settings

# SQLALCHEMY_DATABASE_URL = os.getenv(
#     "DATABASE_URL",
#     "postgresql://postgres:Bringt#1270@localhost:5432/dockert"
# )
engine = create_async_engine(settings.DATABASE_URL,echo=settings.DEBUG)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False, # Crucial for async to prevent lazy-loading errors
    autocommit=False,
    autoflush=False,
)
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
