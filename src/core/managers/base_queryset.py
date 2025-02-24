#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:31"

from django.db import models


class BaseQuerySet(models.QuerySet):
    def hard_delete(self):
        return super().delete()