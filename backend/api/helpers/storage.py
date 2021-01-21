from google.cloud import datastore
import config as c
from typing import Dict
import time

class Storage:

    def __init__(self):
        self.GOOGLE_CLOUD_PROJECT = c.GOOGLE_CLOUD_PROJECT
        self.client = datastore.Client(self.GOOGLE_CLOUD_PROJECT)
        self.KIND = c.KIND

    def _doc(self, **kwargs) -> Dict[str, object]:
        doc = {}
        doc['updated_on'] = time.time()
        doc['source'] = kwargs.get('source')
        doc['source_url'] = kwargs.get('source_url')
        doc['headline'] = kwargs.get('headline')
        doc['story_url'] = kwargs.get('story_url')
        doc['short_desc'] = kwargs.get('short_desc') or None
        doc['category'] = kwargs.get('category') or 'Misc'
        return doc

    def _put(self, entity:object, doc:dict):
        with self.client.transaction():
            entity.update(doc)
            self.client.put(entity)

    def _create(self, **kwargs):
        KIND = self.KIND
        NAMESPACE = kwargs.get('topic')
        id = int(time.time())
        key = self.client.key(KIND, id, namespace=NAMESPACE)
        entity = self.client.get(key)
        entity = datastore.Entity(key=key)
        print(kwargs)
        self._put(entity, kwargs)

    def update(self, **kwargs):
        self._create(**kwargs)
