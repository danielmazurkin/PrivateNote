from sqlalchemy import Column
from sqlalchemy import event
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Boolean

from core.database import Base


class Note(Base):
    """Описываю класс с запиской."""

    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    hash = Column(Text, nullable=True)
    is_view = Column(Boolean, nullable=True)


@event.listens_for(Note, "before_insert")
def event_note_create_with_hash(mapper, connect, target):
    """Событие, которое формирует hash для каждой заметки."""
    target.hash = str(hash(target.text))
