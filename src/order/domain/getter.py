#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:27"

from typing import List

from core.base.base_getter import BaseGetter
from order.converter.order_to_order_data_converter import OrderToOrderDataConverter
from order.dataclasses.order import OrderData
from order.models.order import Order


class OrderGetter(BaseGetter):
    @classmethod
    def get_order_details(cls, order_id):
        """
        Get order details by order_id
        """
        return Order.objects.get_order_details(order_id)

    @classmethod
    def get_orders_by_user(cls, user_id: int, order_status: List[int]) -> List[OrderData]:
        """
        Get orders by user_id and order_status
        """
        user_orders = Order.objects.get_orders_by_user(user_id, order_status)
        user_orders_converted = OrderToOrderDataConverter().convert_list(user_orders)
        return user_orders_converted