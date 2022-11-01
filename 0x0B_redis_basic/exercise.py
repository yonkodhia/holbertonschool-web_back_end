#!/usr/bin/env python3

import uuid
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps

class Cache:
    """ create a cache class """

           def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store the input data in Redis using a random key. """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
