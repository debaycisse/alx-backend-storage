#!/usr/bin/env python3
"""This module houses the definition of a function, named update_topics"""


def update_topics(mongo_collection, name, topics):
    """
    updates or create a document using the value found in name for a name
    attribute and value found in topics for a topics key

    Args:
        mongo_collection - the collection that stores the document
        name - value to store in the name's key
        topics - value to store in the topics' key
    """
    data = {'$set': {'name': name, 'topics': topics}}
    mongo_collection.update_one({'name': name}, data, upsert=True)
