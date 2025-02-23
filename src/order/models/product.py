#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "14:51"

from django.db import models

from core.models import BaseTimeStampedModel
from order.managers.products import ProductManager


class Product(BaseTimeStampedModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    objects = ProductManager()

    class Meta:
        db_table = 'products'