from google.cloud import datastore
from . import config as c
from typing import Dict
import time
from datetime import datetime as dt
class Storage:

    def __init__(self):
        self.project_id = c.GOOGLE_CLOUD_PROJECT
        self.client = datastore.Client(self.project_id)
        self.kind = c.KIND
        self.namespace = c.NAMESPACE

    def _doc(self, data):
        doc = {}
        doc['updated_on'] = str(time.time())
        doc['source'] = data.get('source') or 'unknown'
        doc['source_url'] = data.get('source_url')
        doc['headline'] = data.get('headline')
        doc['story_url'] = data.get('story_url')
        doc['short_desc'] = data.get('short_desc') or 'N/A'
        doc['category'] = data.get('category') or 'Misc'
        return doc

    def _put(self, entity, doc):
        with self.client.transaction():
            entity.update(doc)
            self.client.put(entity)

    def _create(self, data):
        id = str(dt.now()).replace(" ", "|")
        key = self.client.key(self.kind, id, namespace=self.namespace)
        entity = self.client.get(key)
        entity = datastore.Entity(key=key)
        article = self._doc(data)
        self._put(entity, article)

    def update(self, data):
        self._create(data)
    
    def fetch(self, filters):
        if not filters:
            q = self.client.query(kind=self.kind,namespace=self.namespace)
        else:
            q = self.client.query(kind=self.kind,namespace=self.namespace)
            for filter in filters.keys():
                q.add_filter(filter,'=', filters.get(filter))
        # TODO: Decide on pagination and add a limit to fetch
        queried = list(q.fetch())
        return queried

