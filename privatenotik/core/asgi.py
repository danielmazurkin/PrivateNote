import os


ASGI_SERVER_PORT = int(os.getenv('ASGI_SERVER_PORT', default=3400))
ASGI_SERVER_HOST = os.getenv('ASGI_SERVER_HOST', default='localhost')
ASGI_SERVER_PROTOCOL = os.getenv('ASGI_SERVER_PROTOCOL', default='http')
BASE_URL = f'{ASGI_SERVER_PROTOCOL}://{ASGI_SERVER_HOST}:{ASGI_SERVER_PORT}'
