from abc import ABC

import requests

from httpclient.httpclient_private_notik import HttpClientPrivateNotik


class BaseGatewayAPI(ABC):
    """Базовый класс для гейтвеев."""

    query = None
    method = None
    http_client = HttpClientPrivateNotik()

    @classmethod
    def send_request(cls, data=None):
        """Метод для отправки запроса."""
        request_info = cls.http_client.get_uri(url_api=cls.query, method=cls.method, data=data)
        res = requests.request(**request_info)
        return res
