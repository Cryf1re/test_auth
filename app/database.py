from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.config import get_settings
from contextlib import asynccontextmanager
from passlib.context import CryptContext
from sqlalchemy.orm import DeclarativeBase
import asyncio
from app import models # type: ignore


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()


class Base(DeclarativeBase):

    pass

async_engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    pool_size=10,
    max_overflow=20,
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


@asynccontextmanager
async def get_async_session():
    async with async_session() as session:
        yield session


async def init_models():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_models())