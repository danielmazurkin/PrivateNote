from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from notes.models import Note


NoteValidator = sqlalchemy_to_pydantic(Note)
