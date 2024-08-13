#!/usr/bin/env python3
"""This module provides some statistics from the collection,
named nginx in a database, named logs"""
import pymongo

client = pymongo.MongoClient()
db = client['logs']
nginx_col = db['nginx']
status_checked = nginx_col.count_documents({'method': 'GET',
                                            'path': '/status'})
methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

print('{} logs'.format(nginx_col.count_documents({})))
print('Methods:')
for method in methods:
    counter = nginx_col.count_documents({'method': method})
    print('\tmethod {}: {}'.format(method, counter))
print('{} status check'.format(status_checked))
