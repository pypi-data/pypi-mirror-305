from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncAttrs,
)
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy import select
from datetime import datetime
from .logger import configure_logger
from loguru import logger
import os


configure_logger()


class Base(AsyncAttrs, DeclarativeBase):
    pass


class LongUrl(Base):
    __tablename__ = "long_url"
    long_id = Column(Integer, primary_key=True)
    long_value = Column(String(250), unique=True, nullable=False)


class ShortUrl(Base):
    __tablename__ = "short_url"
    short_id = Column(Integer, primary_key=True)
    short_value = Column(String(250), nullable=False)


class UrlMapping(Base):
    __tablename__ = "url_mapping"
    short_id = Column(Integer, ForeignKey("short_url.short_id"), primary_key=True)
    long_id = Column(Integer, ForeignKey("long_url.long_id"), nullable=False)
    expiration = Column(Integer, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    short_url = relationship("ShortUrl", backref="url_mappings")
    long_url = relationship("LongUrl", backref="url_mappings")


class DataBase:
    def __init__(self):
        database_url = f"postgresql+asyncpg://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}"
        self.async_engine = create_async_engine(database_url, echo=True, future=True)
        self.async_session = async_sessionmaker(
            bind=self.async_engine, class_=AsyncSession, expire_on_commit=False
        )

    async def __aenter__(self):
        self.session = self.async_session()
        return self

    async def get_long_url(self, short_value):
        try:
            logger.debug(f"Start select a long_url from a short_url: {short_value}")
            result = await self.session.execute(
                select(LongUrl)
                .join(UrlMapping)
                .join(ShortUrl)
                .where(ShortUrl.short_value == short_value)
            )
            long_url = result.scalars().first()
            if long_url is not None:
                logger.debug(
                    f"long_url is not None return value: {long_url.long_value}"
                )
                return long_url.long_value
            logger.debug("long_url is None return value: None")
            return None
        except Exception as e:
            logger.error(f"An error occurred while fetching long URL: {e}")
            return None

    async def get_expiration(self, short_value):
        try:
            logger.debug(f"Start select a expiration from a short_url: {short_value}")
            result = await self.session.execute(
                select(UrlMapping)
                .join(ShortUrl)
                .where(ShortUrl.short_value == short_value)
            )
            url_mapping = result.scalars().first()
            if url_mapping is not None:
                expiration, date = url_mapping.expiration, url_mapping.date
                create_time = date.hour
                current_time = datetime.now().time().hour
                returned_value = max(int((create_time + expiration) - current_time), 0)
                logger.debug(f"expiration is not None return value: {returned_value}")
                return returned_value
            logger.debug("expiration is None return value: None")
            return None
        except Exception as e:
            logger.error(f"An error occurred while fetching long URL: {e}")
            return None

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.aclose()
