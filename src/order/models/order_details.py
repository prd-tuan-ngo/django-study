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
from order.managers.order_details import OrderDetailsManager


class OrderDetail(BaseTimeStampedModel):
    order = models.ForeignKey('Orders', related_name="order_details", on_delete=models.DO_NOTHING, db_constraint=False)
    product = models.ForeignKey('Products', on_delete=models.DO_NOTHING, db_constraint=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    objects = OrderDetailsManager()


    def __str__(self):
        return self.order_id

    class Meta:
        db_table = 'order_details'
        indexes = [
            models.Index(fields=["order_id"], name="idx_order_details_order_id"),
            models.Index(fields=["product_id"], name="idx_order_details_product_id"),
        ]