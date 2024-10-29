import sys

from httpx import Client, RequestError
from ts_pip_scan import __version__

class ApiClient:
    def __init__(self, base_url: str, api_key: str):
        self._base_url = base_url
        self._api_key = api_key
        self._client = None
        self._headers = {'Accept': 'application/json',
                         "Content-Type": "application/json",
                         'User-Agent': f'ts-pip-scan/{__version__}',
                         'x-api-key': self._api_key
                         }
    @property
    def client(self):
        if self._client is None:
            self._client = Client(base_url=self._base_url, headers=self._headers)
        return self._client

    def post_scan(self, scan_data):
        try:
            res = self.client.post('/core/scans', json=scan_data)
        except RequestError as exc:
            print(f"RequestError: {exc}")
            sys.exit(1)

        if res.is_success:
            result = res.json()
            scan_id = result['scanId']
            print(f'Scan successfully posted. Scan ID: {scan_id}')
            return result
        else:
            print(f'Failed to post scan data {res.request.url}: {res.status_code} error: {res.text}')
            sys.exit(1)


    def get_scan(self, scan_id) -> dict:
        res = self.client.get(f'/core/scans/{scan_id}')
        if res.is_success:
            return res.json()
        else:
            print(f'Failed to get scan data {res.request.url}: {res.status_code} error: {res.text}')
            sys.exit(1)
