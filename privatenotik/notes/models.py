from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import event
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from core.asgi import ASGI_SERVER_HOST
from core.asgi import ASGI_SERVER_PORT
from core.database import Base


class Note(Base):
    """Описываю класс с запиской."""

    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    hash = Column(Text, nullable=True, default=False)
    is_view = Column(Boolean, nullable=True)

    def create_link_by_hash(self):
        return f'{ASGI_SERVER_HOST}:{ASGI_SERVER_PORT}/notes/note?hash_note={self.hash}'


@event.listens_for(Note, "before_insert")
def event_note_create_with_hash(mapper, connect, target):
    """Событие, которое формирует hash для каждой заметки."""
    target.hash = str(hash(target.text))
