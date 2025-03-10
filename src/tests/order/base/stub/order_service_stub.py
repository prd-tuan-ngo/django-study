# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "22:10"

from typing import List

from order.constants.order import OrderStatus
from order.dataclasses.order import OrderData
from tests.base.mock.base_stub import BaseStub


class StubOrderService(BaseStub):
    def __init__(self):
        super().__init__()

    @classmethod
    def get_orders_by_user_with_new_status(cls, user_id: int, order_status: List[int]) -> List[OrderData]:
        return [
            OrderData(id=1, order_uuid="uuid_1231", user_id=1111, status=OrderStatus.NEW),
            OrderData(id=2, order_uuid="uuid_1232", user_id=1112, status=OrderStatus.NEW)
        ]

    @classmethod
    def get_orders_with_raise_exception(cls, user_id: int, order_status: List[int]) -> List[OrderData]:
        raise Exception("Stub raise exception")