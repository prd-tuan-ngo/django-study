# Copyright (C) 2025 paradox.ai
#
# Release: 2.4.9
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "21:32"

from typing import List

from order.constants.order import OrderStatus
from order.models import Order
from tests.base.base_stub import BaseStub
from tests.factory import OrderFactory


class StubOrderGetter(BaseStub):
    def __init__(self):
        super().__init__()

    @classmethod
    def get_orders_by_user_with_new_status(cls, user_id: int, order_status: List[int]) -> List[Order]:
        return [
            OrderFactory.build(id=1, order_uuid="uuid_1231", user_id=1111, status=OrderStatus.NEW),
            OrderFactory.build(id=2, order_uuid="uuid_1232", user_id=1112, status=OrderStatus.NEW)
        ]

    @classmethod
    def get_orders_by_user_with_all_status(cls, user_id: int, order_status: List[int]) -> List[Order]:
        return [
            OrderFactory.build(id=1, order_uuid="uuid_1231", user_id=1111, status=OrderStatus.NEW),
            OrderFactory.build(id=2, order_uuid="uuid_1232", user_id=1112, status=OrderStatus.NEW),
            OrderFactory.build(id=3, order_uuid="uuid_1232", user_id=1112, status=OrderStatus.COMPLETED)
        ]