# Copyright (C) 2025 paradox.ai
#
# Release: 2.4.9
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:37"

import uuid
from collections import defaultdict

from order.dataclasses.order import OrderDetailData
from order.dataclasses.shipping import ShippingOrderDetails, ShippingOrder
from order.intergrations.shipping.base_shipping_adapter import IShippingAdapter


class FakeShippingAdapter(IShippingAdapter):
    def __init__(self):
        self.internal_store_shipping_orders: dict = defaultdict(ShippingOrder)

    def create_shipping_order(self, order_detail: OrderDetailData) -> ShippingOrder:
        shipping_order_fake: ShippingOrder = ShippingOrder(
            order_uuid=order_detail.order.order_uuid,
            shipping_order_uuid=str(uuid.uuid4()),
            provider=9999,
            status=1
        )
        self.internal_store_shipping_orders[shipping_order_fake.shipping_order_uuid] = shipping_order_fake
        return shipping_order_fake


    def get_shipping_order(self, shipping_order_uuid: str) -> ShippingOrderDetails:
        return self.internal_store_shipping_orders.get(shipping_order_uuid)

