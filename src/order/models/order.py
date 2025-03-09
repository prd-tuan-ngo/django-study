#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "14:51"

from django.db import models

from core.models import BaseTimeStampedModel
from order.managers.orders import OrdersManager


class Order(BaseTimeStampedModel):
    order_uuid = models.CharField(max_length=100)
    user_id =  models.IntegerField()
    status = models.IntegerField(max_length=100)

    objects = OrdersManager()

    class Meta:
        db_table = 'orders'