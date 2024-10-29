import time

import requests
from requests.exceptions import HTTPError, RequestException


class RequestHandler:
    def __init__(self, base_url, headers=None, rate_limit=5, max_retries=3, backoff_factor=2):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.rate_limit = rate_limit
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.last_request_time = 0

    def _rate_limit(self):
        if not self.rate_limit:
            return
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit:
            wait_time = self.rate_limit - elapsed
            time.sleep(wait_time)
        self.last_request_time = time.time()

    def _handle_response(self, response, method):
        try:
            response.raise_for_status()
            if method == 'DELETE':
                return response.text
            return response.json()
        except HTTPError as http_err:
            # Provide detailed error information
            raise RuntimeError(f"HTTP error occurred: {http_err} - {response.text}") from http_err
        except ValueError:
            # If JSON decoding fails
            raise RuntimeError(f"Failed to decode JSON: {response.text}")

    def _request(self, method, endpoint, **kwargs):
        self._rate_limit()
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        retry_count = 0
        with requests.Session() as session:
            session.headers.update(self.headers)
            while retry_count < self.max_retries:
                try:
                    response = session.request(method, url, **kwargs)
                    if response.status_code == 429:  # Too Many Requests
                        wait_time = 5 * (self.backoff_factor ** retry_count)
                        time.sleep(wait_time)
                        retry_count += 1
                        continue
                    return self._handle_response(response, method)
                except (RequestException, HTTPError) as err:
                    retry_count += 1
                    if retry_count >= self.max_retries:
                        raise RuntimeError(f"Request failed after {self.max_retries} attempts: {err}")

    def get(self, endpoint, params=None):
        return self._request('GET', endpoint, params=params)

    def post(self, endpoint, data=None, params=None, json=None):
        return self._request('POST', endpoint, data=data, params=params, json=json)

    def put(self, endpoint, data=None, params=None, json=None):
        return self._request('PUT', endpoint, data=data, params=params, json=json)

    def delete(self, endpoint, params=None):
        return self._request('DELETE', endpoint, params=params)
    
    def patch(self, endpoint, data=None, params=None, json=None):
        return self._request('PATCH', endpoint, data=data, params=params, json=json)
