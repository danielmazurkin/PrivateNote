from fastapi import APIRouter
from sqlalchemy.orm import Session

from core.database import engine
from notes.models import Note
from notes.validators import NoteSerializer


router = APIRouter(prefix='/notes')


@router.post('/note', response_model=NoteSerializer)
async def create_note(note: NoteSerializer):
    """Создание заметки."""
    with Session(bind=engine) as session:
        session.add(Note(**note.dict()))
        session.commit()
    return note


@router.get('/note')
async def get_note_text(hash_note: str):
    """Получение текста по заметке."""
    ...


@router.get('/link')
async def link_note(note_id: int) -> str:
    """Cформировать ссылку с хэшом."""
    with Session(bind=engine) as session:
        note = session.query(Note).filter(Note.id == note_id).first()
        link_by_hash = note.create_link_by_hash()

    return link_by_hash
