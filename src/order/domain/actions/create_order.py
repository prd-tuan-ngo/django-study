#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:53"

import uuid
from typing import Dict, Optional, Any

from django.db import transaction

from order.constants.order import OrderStatus
from order.dataclasses.order import OrderData
from order.dataclasses.shipping import ShippingOrder


class CreateOrderAction:
    def create_order(self, user_id: int, order_data: Dict) -> OrderData:
        with transaction.atomic():
            order = self.__save_order(user_id, order_data)
            self.__save_order_details(order.order_uuid, order_data=order_data)
        if not order:
            raise Exception("Failed to create order")
        # shipping_provider = order_data.get("shipping_provider")
        # shipping_order = self.__create_shipping_order(order, shipping_provider)
        # if not shipping_order:
        #     raise Exception("Failed to create shipping order")
        # self.__save_shipping_order(shipping_order)
        return order

    def __save_order(self, user_id: int, order_data: Dict[str, Any]) -> OrderData:
        # TODO Save an order to database
        from order.models import Order

        base_order = Order.objects.create(
            user_id=user_id,
            order_uuid=str(uuid.uuid4()),
            status=OrderStatus.NEW
        )
        return base_order

    def __create_shipping_order(self, order: OrderData, shipping_provider: int) -> ShippingOrder:
        # TODO create shipping order on 3rd party service
        pass

    def __save_shipping_order(self, shipping_order: ShippingOrder):
        # TODO save shipping order to database
        pass

    def __save_order_details(self, order_uuid, order_data):
        pass
