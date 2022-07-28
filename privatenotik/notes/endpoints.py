from fastapi import APIRouter

from core.database import engine
from notes.validators import NoteSerializer
from notes.models import Note
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/notes')


@router.post('/note', response_model=NoteSerializer)
async def create_note(note: NoteSerializer):
    async with AsyncSession(bind=engine) as session:
        session.add(Note(**note.dict()))
        await session.commit()
    return note
