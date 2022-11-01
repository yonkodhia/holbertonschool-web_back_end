#!/usr/bin/env python3

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """ create a cache class """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
