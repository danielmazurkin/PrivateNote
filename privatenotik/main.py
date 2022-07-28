import uvicorn
import asyncio
from core.asgi import ASGI_SERVER_PORT, ASGI_SERVER_HOST
from core.database import create_init_async_db
from notes.endpoints import router as router_notes
from fastapi import FastAPI

app = FastAPI()

app.include_router(router_notes)


if __name__ == '__main__':
    asyncio.run(create_init_async_db())
    uvicorn.run('main:app', port=ASGI_SERVER_PORT, host=ASGI_SERVER_HOST, debug=True)
