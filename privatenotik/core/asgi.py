import os


ASGI_SERVER_PORT = int(os.getenv('ASGI_SERVER_PORT', default=81))
ASGI_SERVER_HOST = os.getenv('ASGI_SERVER_HOST', default='127.0.0.1')

