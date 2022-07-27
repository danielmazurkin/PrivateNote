from core.database import Base
from sqlalchemy import Integer, Column, String, Text


class Note(Base):
    """Описываю класс с запиской."""

    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    hash = Column(Text)
