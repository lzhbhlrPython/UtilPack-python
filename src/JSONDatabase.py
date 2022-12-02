# Amazing Database System based on JSON
# Author: @lzhbhlrPython

import json
import time
import uuid
import os

class Database:
    def __init__(self, name):
        self.name = name
        self.all = {'meta':{}, 'data':{}}
        self.meta = self.all['meta']
        self.data = self.all['data']
        self.meta['name'] = name
        self.meta['uuid'] = str(uuid.uuid1())
        self.meta['created'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.meta['last_modified'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.meta['name'] = name
        self.meta['by'] = 'ADSBJ'
    def add(self, key, value):
        if key in self.data:
            raise KeyError('Key already exists')
        self.data[key] = value
        self.meta['last_modified'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    def delete(self, key):
        if key not in self.data:
            raise KeyError('Key does not exist')
        del self.data[key]
        self.meta['last_modified'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    def update(self, key, value):
        if key not in self.data:
            raise KeyError('Key does not exist')
        self.data[key] = value
        self.meta['last_modified'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    def get(self, key):
        if key not in self.data:
            raise KeyError('Key does not exist')
        return self.data[key]
    def save(self):
        with open(self.name+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.all, f, ensure_ascii=False, indent=4)
    def load(self):
        if self.name+'.json' not in os.listdir():
            raise FileNotFoundError('File not found')
        with open(self.name+'.json', 'r', encoding='utf-8') as f:
            self.all = json.load(f)
            self.meta = self.all['meta']
            self.data = self.all['data']
    def __str__(self):
        return str(self.all)
    def __dict__(self):
        return self.all
    def __len__(self):
        return len(self.data)
    def __iter__(self):
        return iter(self.data)
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, value):
        if key in self.data:
            self.update(key, value)
        else:
            self.add(key, value)
    def __delitem__(self, key):
        self.delete(key)
    def __contains__(self, key):
        return key in self.data
    
    @staticmethod
    def load_database(name):
        db = Database(name)
        db.load()
        return db