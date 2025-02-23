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
from order.managers.orders import OrdersManager


class Order(BaseTimeStampedModel):
    order_uuid = models.CharField(max_length=100, unique=True)
    user_id =  models.IntegerField()
    status = models.CharField(max_length=100)

    objects = OrdersManager()

    class Meta:
        db_table = 'orders'