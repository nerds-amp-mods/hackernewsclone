import requests
import os
from errors import ClientError

default_api_url = 'http://localhost:5000'

class Client:
    def __init__(self, **kwargs):
        self.init(**kwargs)

    def init(self, **kwargs):
        api_token = kwargs.get('api_token')
        api_url = kwargs.get('api_url')
        if api_token is None:
            raise ClientError('Initilization the client failed, missing API Token')
        else:
            self.api_url = api_url or default_api_url
            self.token = api_token 
            # self.headers = {'Authorization': f'Bearer {self.token}'} 
            # headers need to be implemented yet
            self.update_url = self.api_url + '/add'

    def update(self, article: dict):
        # r = requests.post(update_url, headers=self.headers, json=article)
        r = requests.post(update_url, json=article)
        status = r.status_code 
        if  status == 200:
            return r.json()
        else:
            raise Exception(f'Failed to update with {status_code}')
    

