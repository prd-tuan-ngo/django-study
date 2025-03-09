#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "19:22"

from core.base.converter.base_converter import BaseConverter
from order.dataclasses.order import OrderData
from order.models import Order


class OrderToOrderDataConverter(BaseConverter[Order, OrderData]):
    def _convert_hook(self, order: Order) -> OrderData:
        order_data = OrderData(
            id = order.id,
            order_uuid = order.order_uuid,
            user_id = order.user_id,
            status = order.status
        )
        return order_data