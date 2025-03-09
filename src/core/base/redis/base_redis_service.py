#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "13:51"

from datetime import datetime

import pytz
from django.conf import settings
from redis.client import StrictRedis


class BaseRedisService:
    PREFIX = None
    client: StrictRedis | None = None

    def __init__(self, **kwargs):
        from django_redis import get_redis_connection

        self.client = get_redis_connection(settings.REDIS_DATA_CACHE_SETTING_NAME)
        if "prefix" in kwargs:
            self.PREFIX = kwargs.get("prefix")

    def flush_db(self):
        self.client.flushdb()

    def make_key(self, *args):
        if self.PREFIX:
            return "{}:{}".format(self.PREFIX, ":".join(str(v) for v in args))
        return ":".join(str(v) for v in args)

    def __getattr__(self, item):
        """
        Call directly to client without redefine fn
        """
        fn = getattr(self.client, item, None)
        if fn is None or not callable(fn):
            raise Exception(f"Method {item} not found")
        return fn
