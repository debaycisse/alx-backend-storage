#!/usr/bin/env python3
"""This module houses the definition of the get_page function, which gets
the content of a given url and returns the html content of the passed url"""

from functools import wraps
from typing import Callable
import redis
import requests


def track_url(func: Callable) -> Callable:
    """
    tracks the number of times a url is
    visited by its passed function

    Args:
        func - the function that visits the url

    Return:
        the output of the wrapped function
    """

    redis_client = redis.Redis(db=1)

    @wraps(func)
    def wrapper(url: str) -> str:
        """
        wraps around the get_page function and tracks
        the url visited and record how many number of
        times the url has been visited

        Args:
            url - the url to be visited

        Returns:
            the output of the passed function (that's get_page)
        """
        k = 'count:{0}'.format(url)
        if not redis_client.get(k):
            redis_client.setex(k, 10, 1)
        else:
            redis_client.incr(k, 1)
        return func(url)
    return wrapper


@track_url
def get_page(url: str) -> str:
    """
    uses the requests module to obtain the HTML content
    of a particular URL and returns it.

    Args:
        url - the url address to which a request is to be sent

    Returns:
        the content that is returned or gotten from the request
    """
    req = requests.get(url)
    if req.status_code == 200:
        return req.text
    raise requests.exceptions.InvalidURL('Invalid url')
