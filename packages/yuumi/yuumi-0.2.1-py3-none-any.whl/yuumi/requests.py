import requests
import time

class RequestHandler:
    def __init__(self, base_url, headers, rate_limit=5):
        self.base_url = base_url
        self.headers = headers
        self.rate_limit = rate_limit
        self.last_request_time = 0

    def _rate_limit(self):
        if self.rate_limit:
            elapsed = time.time() - self.last_request_time
            wait_time = max(0, self.rate_limit - elapsed)
            if wait_time > 0:
                time.sleep(wait_time)
        self.last_request_time = time.time()

    def _request(self, method, endpoint, **kwargs):
        self._rate_limit()
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        if method == 'DELETE':
            return response.text
        return response.json()

    def get(self, endpoint, params=None):
        return self._request('GET', endpoint, params=params)

    def post(self, endpoint, data, params=None):
        return self._request('POST', endpoint, data=data, params=params)

    def put(self, endpoint, data, params=None):
        return self._request('PUT', endpoint, data=data, params=params)

    def delete(self, endpoint, params=None):
        return self._request('DELETE', endpoint, params=params)
    
    def patch(self, endpoint, data, params=None):
        return self._request('PATCH', endpoint, data=data, params=params)