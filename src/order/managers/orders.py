#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:30"

from core.managers import BaseManager, BaseQuerySet


class OrderQuerySet(BaseQuerySet):
    pass

class OrdersManager(BaseManager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)