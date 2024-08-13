#!/usr/bin/env python3
"""This module houses the definition of a function, named schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """
    returns a list of school documents that have a specific topic

    Args:
        mongo_collection - the collection to lookup for the documents
        topic - the specific attribute of a school document to look for

    Returns:
        list of all school document that contains the topic
    """
    return mongo_collection.find({'topics': {'$elemMatch': {'$eq': topic}}})
