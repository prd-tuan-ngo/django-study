#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "20:37"

from unittest import TestCase

import pytest


@pytest.mark.django_db(transaction=True, databases=["default"])
class BaseTest(TestCase):
    pass