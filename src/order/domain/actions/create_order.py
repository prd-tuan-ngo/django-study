#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:53"

from typing import Dict, Optional, Any

from django.db import transaction

from order.dataclasses.order import Order
from order.dataclasses.shipping import ShippingOrder


class CreateOrderAction:
    def create_order(self, order_data: Dict):
        with transaction.atomic:
            order = self.__save_order(order_data)
        if not order:
            raise Exception("Failed to create order")
        shipping_provider = order_data.get("shipping_provider")
        shipping_order = self.__create_shipping_order(order, shipping_provider)
        if not shipping_order:
            raise Exception("Failed to create shipping order")
        self.__save_shipping_order(shipping_order)
        return order

    def __save_order(self, order_data: Dict[str, Any]) -> Order:
        # TODO Save an order to database
        pass

    def __create_shipping_order(self, order: Order, shipping_provider: int) -> ShippingOrder:
        # TODO create shipping order on 3rd party service
        pass

    def __save_shipping_order(self, shipping_order: ShippingOrder):
        # TODO save shipping order to database
        pass
