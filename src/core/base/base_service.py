#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:14"

from core.dataclasses.user import User


class BaseService:
    @classmethod
    def get_user(cls) -> User:
        """
        Get user
        """
        return User(user_id=55555, name="hardcoded_user")
