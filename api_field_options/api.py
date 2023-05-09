import requests
import json
from requests.auth import HTTPBasicAuth
from config import *


class Api:
    @staticmethod
    def get_request(request_url, request_headers, params):
        response = requests.request(
            "GET",
            request_url,
            headers=request_headers,
            params=params,
            auth=HTTPBasicAuth(USERNAME, API_TOKEN)
        )
        return json.loads(response.content)

    @staticmethod
    def post_request(request_url, request_headers, data):
        response = requests.request(
            "POST",
            request_url,
            headers=request_headers,
            data=data,
            auth=HTTPBasicAuth(USERNAME, API_TOKEN)
        )
        return json.loads(response.content)

    @staticmethod
    def delete_request(request_url, params):
        response = requests.request(
            "DELETE",
            request_url,
            params=params,
            auth=HTTPBasicAuth(USERNAME, API_TOKEN)
        )

        return json.loads(response.content)