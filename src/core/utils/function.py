#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:35"

from functools import wraps
from logging import Logger
from typing import Callable, Optional

from django.db import transaction


def safe_executor(with_transaction=False, re_raise=False, default=None, default_factory=None, with_log=False):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            kwargs.update(
                with_transaction=with_transaction,
                re_raise=re_raise,
                default=default,
                default_factory=default_factory,
                with_log=with_log,
            )
            return safe_execute(func, *args, **kwargs)

        return wrapped

    return decorator


def safe_execute(func, *args, **kwargs):
    with_transaction = kwargs.pop("with_transaction", False)
    re_raise = kwargs.pop("re_raise", False)
    default = kwargs.pop("default", None)
    default_factory: Optional[Callable] = kwargs.pop("default_factory", None)
    with_log = kwargs.pop("with_log", True)
    try:
        if with_transaction:
            with transaction.atomic():
                result = func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)
    except Exception as e:
        if with_log:

            Logger.error(str(e))
        if re_raise:
            raise e
        if default_factory is not None:
            return default_factory()
        return default
    return result


def skip_execute(when: Callable, default=None):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if when(*args, **kwargs):
                    return default
            except:
                pass
            return func(*args, **kwargs)

        return wrapped

    return decorator