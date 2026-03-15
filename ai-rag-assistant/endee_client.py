import os
import requests
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

class EndeeError(Exception):
    pass

class Client:
    def __init__(self, host: str = 'http://localhost:8080', token: Optional[str] = None):
        self.host = host.rstrip('/')
        self.base_url = f'{self.host}/api/v1'
        self.token = token or os.getenv('ENDEE_TOKEN')
        self.headers = {'Content-Type': 'application/json'}
        if self.token:
            self.headers['Authorization'] = self.token
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        url = f'{self.base_url}/{endpoint}'
        try:
            resp = self.session.request(method, url, **kwargs)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            raise EndeeError(f'Endee API error: {e}')

    def list_collections(self) -> List[str]:
        data = self._request('GET', 'index/list')
        return [item['name'] for item in data]

    def create_collection(self, name: str, dimension: int = 384, metric: str = 'cosine'):
        payload = {'name': name, 'dimension': dimension, 'metric': metric}
        self._request('POST', 'index/create', json=payload)

    def insert(self, collection_name: str, vectors: List[Dict[str, Any]]):
        payload = {'collection_name': collection_name, 'vectors': vectors}
        self._request('POST', 'index/upsert', json=payload)

    def search(self, collection_name: str, vector: List[float], top_k: int = 3) -> List[Dict[str, Any]]:
        payload = {'collection_name': collection_name, 'vector': vector, 'top_k': top_k}
        data = self._request('POST', 'index/query', json=payload)
        return data  # Assume [{'id': str, 'score': float, 'metadata': dict}, ...]

