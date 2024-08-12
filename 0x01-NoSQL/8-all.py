#!/usr/bin/env python3
"""This module houses the definition of a function, named list_all"""


def list_all(mongo_collection):
    """retrieves all documents in a given collectin

    Args:
        mongo_collection - the collection from which documents are retrieved

    Returns:
        the list of all found documents in the passed collection
    """
    return mongo_collection.find()
