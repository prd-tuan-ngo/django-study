#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:04"

from abc import abstractmethod, ABC

from order.dataclasses.order import OrderDetailData
from order.dataclasses.shipping import ShippingOrder, ShippingOrderDetails


class IShippingAdapter(ABC):
    @abstractmethod
    def create_shipping_order(self, order_detail: OrderDetailData) -> ShippingOrder:
        ...

    @abstractmethod
    def get_shipping_order(self, shipping_order_uuid: str) -> ShippingOrderDetails:
        ...