import os


ASGI_SERVER_PORT = int(os.getenv('ASGI_SERVER_PORT', default=3400))
ASGI_SERVER_HOST = os.getenv('ASGI_SERVER_HOST', default='localhost')
