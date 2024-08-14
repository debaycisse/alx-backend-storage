#!/usr/bin/env python3
"""This module houses the definition of a class, named Cache"""

import redis
from uuid import uuid4
from typing import Union


class Cache:
    """This class writes a given string to Redis storage"""

    data_types: Union = Union[bytes, str, int, float]

    def __init__(self):
        """Method creates an instance of Redis and empties it"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: data_types) -> str:
        """Method stores a given data in redis, using
        randomly generated uuid as a key

        Args:
            data - the data to be stored in the redis

        Returns:
            the randomly generated key, which is used for storing data
        """
        k: str = str(uuid4())
        self._redis.set(k, data)
        return k
