import uvicorn
from core.asgi import ASGI_SERVER_PORT, ASGI_SERVER_HOST
from core.database import engine
from notes.endpoints import router as router_notes
from fastapi import FastAPI

app = FastAPI()

app.include_router(router_notes)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    engine.connect()
    uvicorn.run('core.asgi:app', port=ASGI_SERVER_PORT, host=ASGI_SERVER_HOST)
