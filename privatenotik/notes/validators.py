from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from notes.models import Note


NoteSerializer = sqlalchemy_to_pydantic(Note, exclude=['hash', 'id'])
