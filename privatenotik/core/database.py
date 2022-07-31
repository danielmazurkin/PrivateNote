import os

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base


POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE', default='private')
POSTGRES_USER = os.getenv('POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='12345')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', default='localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', default=5432)
DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DATABASE}"

Meta = MetaData()
Base = declarative_base(metadata=Meta)
engine = create_engine(DB_URL)
