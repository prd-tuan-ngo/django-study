#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:53"

import uuid
from typing import Dict, Any

from django.db import transaction

from order.constants.order import OrderStatus
from order.dataclasses.order import OrderData, OrderDetailData
from order.dataclasses.shipping import ShippingOrder, ShippingOrderDetails
from order.dataclasses.shop import Shop
from order.intergrations.shipping.base_shipping_adapter import IShippingAdapter
from order.intergrations.shipping.shipper_factory import ShippingAdapterFactory
from order.models import Order


class CreateOrderAction:
    def create_order(self, user_id: int, order_data_input: Dict) -> OrderData:
        with transaction.atomic():
            order = self.__save_order(user_id, order_data_input)
            self.__save_order_details(order.order_uuid, order_data=order_data_input)
        if not order:
            raise Exception("Failed to create order")
        order_data_created = OrderData(id=order.id, order_uuid=order.order_uuid, user_id=order.user_id, status=order.status)

        shipping_data = order_data_input.get("shipping_data")
        shipping_order = self.__create_shipping_order(order_data_created, shipping_data)
        if not shipping_order:
            raise Exception("Failed to create shipping order")

        self.__save_shipping_order(shipping_order)

        order_data_created.shipping_order_uuid = shipping_order.shipping_order_uuid

        return order_data_created

    def __save_order(self, user_id: int, order_data: Dict[str, Any]) -> Order:
        # TODO Save an order to database
        from order.models import Order

        base_order = Order.objects.create(
            user_id=user_id,
            order_uuid=str(uuid.uuid4()),
            status=OrderStatus.NEW
        )

        # TODO Save order details to database

        return base_order

    def __create_shipping_order(self,order_data_created: OrderData, shipping_data: dict) -> ShippingOrder:
        # TODO create shipping order on 3rd party service
        shipping_adapter: IShippingAdapter = ShippingAdapterFactory.get_shipping_adapter(shipping_data.get("shipping_provider"))
        order_detail_data = self.__create_order_detail_data_for_shipping_order(order_data_created, shipping_data)
        shipping_order = shipping_adapter.create_shipping_order(order_detail_data)
        return shipping_order


    def __save_shipping_order(self, shipping_order: ShippingOrder):
        # TODO save shipping order to database
        pass

    def __save_order_details(self, order_uuid, order_data):
        pass

    def __create_order_detail_data_for_shipping_order(self, order: OrderData, shipping_data: dict) -> OrderDetailData:
        # TODO create OrderDetailData for shipping order
        return OrderDetailData(order=order,
                               shipping_order=ShippingOrderDetails(shipping_order_uuid=order.shipping_order_uuid),
                               shop=Shop(shop_uuid=shipping_data.get("shop_id")),
                               to_address=shipping_data.get("to_address"),
                               cod_amount=shipping_data.get("cod_amount")
                               )
