from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.database import engine
from notes.models import Note
from notes.validators import NoteSerializer


router = APIRouter(prefix='/notes')


@router.post('/note', response_model=NoteSerializer, status_code=201)
async def create_note(note: NoteSerializer):
    """Создание заметки."""
    with Session(bind=engine) as session:
        session.add(Note(**note.dict()))
        session.commit()
    return note


@router.get('/note')
async def get_note_text(hash_note: str = None) -> str:
    """Получение текста по заметке."""
    with Session(bind=engine) as session:
        note = session.query(Note).filter(Note.hash == hash_note).first()

        if not note or note.is_view:
            raise HTTPException(status_code=404, detail="Note Not found")

        note.is_view = True
        session.add(note)
        session.commit()

        session.refresh(note)
        session.expunge(note)

    return JSONResponse(content=note.text, status_code=200)


@router.get('/link')
async def link_note(note_id: int) -> str:
    """Cформировать ссылку с хэшом."""
    with Session(bind=engine) as session:
        note = session.query(Note).filter(Note.id == note_id).first()

        if not note:
            raise HTTPException(status_code=404, detail="Note not found")

        link_by_hash = note.create_link_by_hash()

    return JSONResponse(content=link_by_hash, status_code=200)
