#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:27"

from typing import List

from django.forms.models import model_to_dict

from core.base.base_getter import BaseGetter
from order.converter.order_to_order_data_converter import OrderToOrderDataConverter
from order.dataclasses.order import OrderData
from order.models.order import Order


class OrderGetter(BaseGetter):
    def get_order_details(self, order_id):
        """
        Get order details by order_id
        """
        return Order.objects.get_order_details(order_id)

    def get_orders_by_user(self, user_id: int, order_status: List[int]) -> List[OrderData]:
        """
        Get orders by user_id and order_status
        """
        user_orders = Order.objects.get_orders_by_user(user_id, order_status)
        user_orders_converted = OrderToOrderDataConverter().convert_list(user_orders)
        return user_orders_converted