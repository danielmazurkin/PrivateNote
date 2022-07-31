
from fastapi import FastAPI
import uvicorn

from core.asgi import ASGI_SERVER_HOST
from core.asgi import ASGI_SERVER_PORT
from notes.endpoints import router as router_notes


app = FastAPI()

app.include_router(router_notes)


if __name__ == '__main__':
    uvicorn.run('main:app', port=ASGI_SERVER_PORT, host=ASGI_SERVER_HOST, debug=True)
