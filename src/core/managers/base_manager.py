#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:31"

from django.db.models import Manager


class BaseManager(Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db)