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
        total_score = sum(sc.get('score') for sc in topics)
        student_avg = None

        if (total_score > 0.0):
            student_avg = total_score / len(topics)
        else:
            student_avg = 0.0

        mongo_collection.update_one(
                                    {'_id': student.get('_id')},
                                    {'$set': {'averageScore': student_avg}})
    return mongo_collection.find().sort('averageScore', -1)
