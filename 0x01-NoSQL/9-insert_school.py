#!/usr/bin/env python3
"""This module houses a definition for a function, namde insert_school"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document in a passed collection.

    Args:
        mongo_collection - the collection, to store the inserted document
        kwargs - list of attributes and their respective values

    Returns:
        the id attribute of the inserted document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
