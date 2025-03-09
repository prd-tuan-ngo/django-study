#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:30"

from typing import List

from core.managers import BaseManager, BaseQuerySet


class OrderQuerySet(BaseQuerySet):
    def belong_to_user(self, user_id: int):
        return self.filter(user_id=user_id)

    def by_statuses(self, statuses: list):
        return self.filter(status__in=statuses)

class OrdersManager(BaseManager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def get_order_details(self, order_id):
        return self.get_queryset().filter(id=order_id).prefetch_related('order_detail').first()

    def get_orders_by_user(self, user_id: int, order_status: list) -> List:
        qs = self.get_queryset().belong_to_user(user_id)
        if order_status:
            qs = qs.by_statuses(order_status)
        return list(qs)