from fastapi import APIRouter

router = APIRouter(prefix='/notes')


@router.get('/')
async def get_main_page_info():
    return {'test': '5'}
