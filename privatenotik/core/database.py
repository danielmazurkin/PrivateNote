import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base


POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE', default='privatenotik')
POSTGRES_USER = os.getenv('POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='12345')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', default='localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', default=5432)

engine = create_async_engine(
    f"postgresql+asyncpg://{POSTGRES_PORT}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DATABASE}", echo=True,
)

Base = declarative_base()
