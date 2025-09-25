from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from config import settings

engine = create_async_engine(settings.DATABASE_URL_async, echo=True)

class Base(DeclarativeBase):
    metadata = MetaData()

session_factory = async_sessionmaker(engine)