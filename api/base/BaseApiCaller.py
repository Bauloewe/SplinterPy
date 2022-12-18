import time

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class BaseApiCaller:

    def call_get(self, url: str, params: dict = {}):
        s = requests.Session()

        params["v"] = int(time.time() * 1000)

        print(params)

        retries = Retry(total=5,
                        backoff_factor=0.1,
                        status_forcelist=[500, 502, 503, 504])
        s.mount('https://', HTTPAdapter(max_retries=retries))

        headers = {
            "Accept-Encoding": "gzip"
        }

        response = s.get(url, params=params,headers=headers)
        json_response = dict()
        if response is not None:
            json_response = response.json()

        return json_response
