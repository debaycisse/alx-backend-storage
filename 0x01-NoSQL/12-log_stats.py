#!/usr/bin/env python3
"""This module provides some statistics from the collection,
named nginx in a database, named logs"""

import pymongo

client = pymongo.MongoClient()
db = client['logs']
nginx_col = db['nginx']
get_method_count = nginx_col.count_documents({'method': 'GET'})
post_method_count = nginx_col.count_documents({'method': 'POST'})
put_method_count = nginx_col.count_documents({'method': 'PUT'})
patch_method_count = nginx_col.count_documents({'method': 'PATCH'})
delete_method_count = nginx_col.count_documents({'method': 'DELETE'})
status_checked = nginx_col.count_documents({
                                            'method': 'GET',
                                            'path': '/status'})

print('{} logs'.format(nginx_col.count_documents({})))
print('Methods:')
print('    method GET: {}'.format(get_method_count))
print('    method POST: {}'.format(post_method_count))
print('    method PUT: {}'.format(put_method_count))
print('    method PATCH: {}'.format(patch_method_count))
print('    method DELETE: {}'.format(delete_method_count))
print('{} status check'.format(status_checked))
