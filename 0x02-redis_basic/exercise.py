#!/usr/bin/env python3
"""This module houses the definition of a class, named Cache"""

import redis
from uuid import uuid4
from typing import Union, Callable


class Cache:
    """This class writes a given string to Redis storage"""

    def __init__(self):
        """Method creates an instance of Redis and empties it"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
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

    def get_str(self, data: bytes) -> str:
        """
        converts a given data to string format or type

        Args:
            data - the given data to be converted

        Returns:
            the string equivalent of the passed data
        """
        return str(data)

    def get_int(self, data: bytes) -> int:
        """
        coverts a given data to an interger form or type

        Args:
            data - the given data to be converted into an integer type

        Returns:
            the integer equivalent of the passed or given data
        """
        return int(data)

    def get(self, key: str,
            fn: Union[Callable[[bytes], Union[str, int]], None] = None
            ) -> Union[None, str, int, bytes]:
        """
        retrieves the value (in its original form other than bytes),
        stored in the passed key

        Args:
            key - the key to the value that is to be retrieved
            fn - a function that should be used for the
            conversion of the retrieved data whose key is passed
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if value is not None and fn is not None:
            return fn(value)
        return value
