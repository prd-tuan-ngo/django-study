#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:34"

from core.managers import BaseQuerySet, BaseManager


class ProductQuerySet(BaseQuerySet):
    pass

class ProductManager(BaseManager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)