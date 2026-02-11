from typing import AsyncGenerator
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import event
from sqlalchemy import Column, Integer, String

# uvicorn app.main:app --reload

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost:5432/concurrency_db"

# объект, который управляет соединениями с базой
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    db: AsyncSession = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


# Модель аккаунта
class Account(Base):
    __tablename__ = "account"

    Account_id = Column(Integer, primary_key=True, index=True)
    balance = Column(Integer, default=0)
