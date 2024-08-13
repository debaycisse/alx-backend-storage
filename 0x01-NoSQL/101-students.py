#!/usr/bin/env python3
"""This module houses the definition of a function, named top_students"""

import pymongo


def top_students(mongo_collection):
    """
    computes average score for all students in mongo_collection

    Args:
        mongo_collection - the collection that contains
        all the students documents

    Returns:
        an ordered (in descending) of the average score of each student
    """
    for student in mongo_collection.find():
        topics = student.get('topics')
        topics_length = len(topics)
        total_score = ()
        mongo_collection.update({'name': student.get('name')}, {'$set': {'averageScore': {'$avg': student.get('topics')[0].get('score')}}})
