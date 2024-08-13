#!/usr/bin/env python3
"""This module provides some statistics from the collection,
named nginx in a database, named logs"""
import pymongo

if (__name__ == '__main__'):
    client = pymongo.MongoClient()
    db = client['logs']
    nginx = db['nginx']
    status_checked = nginx.count_documents({'method': 'GET',
                                                'path': '/status'})
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print('{} logs'.format(nginx.count_documents({})))
    print('Methods:')
    for method in methods:
        counter = nginx.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, counter))
    print('{} status check'.format(status_checked))

    print('IPs:')
    for log in nginx.find():
        c = nginx.count_documents({'ip': log.get('ip')})
        nginx.update_one({'_id': log.get('_id')}, {'$set': {'count': c}})

    top_ten = []
    for obj in nginx.find().sort([('count', pymongo.DESCENDING)]):
        if (len(top_ten) >= 10):
            break
        if (obj.get('ip') in top_ten):
            continue
        top_ten.append(obj.get('ip'))
        print('\t{}: {}'.format(obj.get('ip'), obj.get('count')))
