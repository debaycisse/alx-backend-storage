#!/usr/bin/env python3
"""This module houses the definition of a class, named Cache"""

import redis
from uuid import uuid4
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    increment a number everytime a method in Cache class is called

    Args:
        method - the called method

    Returns:
        the called method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wraps the passed method, executes it, returns
        its output and counts its number of calls

        Args:
            args - the list of argument that is passed to the given method
            kwargs - the list of keyword argument of the given method

        Returns:
            the output of the passed method
        """
        k = method.__qualname__
        _redis = self._redis
        _redis.incr(k, amount=1)
        mt = method(self, *args, **kwargs)
        return mt
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    stores the history of both input argument
    and output value for its passed function

    Args:
        method - the method that is passed to this decorator

    Returns:
        the passed function with its supplied arguments
    """
    _in = f'{method.__qualname__}:inputs'
    _out = f'{method.__qualname__}:outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wraps the passed method, stores its argument and output value in
        a list, executes it and returns its output

        Args:
            args - list of arguments of the passed method
            kwargs - list of keyword arguments of the passed method

        Returns:
            the output value of the given method
        """
        _redis = self._redis
        _redis.rpush(_in, str(args))
        mt = method(self, *args, **kwargs)
        _redis.rpush(_out, mt)
        return mt
    return wrapper


class Cache:
    """This class writes a given string to Redis storage"""

    def __init__(self):
        """Method creates an instance of Redis and empties it"""
        self._redis = redis.Redis(db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
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


def replay(method: Callable) -> None:
    """"""
    @wraps
    def wrapper(self, *args, **kwargs):
        """
        wraps the given method, retrieves its length
        """

