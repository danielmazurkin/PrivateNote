from core.asgi import BASE_URL
from core.singleton import Singleton


class HttpClientPrivateNotik(metaclass=Singleton):
    """Базовый класс для построения запросов."""

    BASE_URL_API = BASE_URL

    @staticmethod
    def _make_request(url_api: str, method: str, params=None, data=None) -> str:
        """На основании этого метода будем делать запрос."""
        if params:
            return f'{HttpClientPrivateNotik.BASE_URL_API}{url_api}?{params}'

        uri = f'{HttpClientPrivateNotik.BASE_URL_API}{url_api}'
        return {'method': method, 'url': uri, 'data': data}

    def get_uri(self, url_api: str, query_param_raw=None, method='GET', data=None) -> str:
        """Обрабатывает запросы."""
        return HttpClientPrivateNotik._make_request(url_api, method, query_param_raw, data)
