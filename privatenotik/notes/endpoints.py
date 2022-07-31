from fastapi import APIRouter
from sqlalchemy.orm import Session

from core.database import engine
from notes.models import Note
from notes.validators import NoteSerializer


router = APIRouter(prefix='/notes')


@router.post('/note', response_model=NoteSerializer)
async def create_note(note: NoteSerializer):
    with Session(bind=engine) as session:
        session.add(Note(**note.dict()))
        session.commit()
    return note


@router.get('/note')
async def get_note(hash_note: str):
    ...

