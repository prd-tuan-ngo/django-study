#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:17"

from typing import List

from order.constants.order import OrderStatus
from order.models import Order
from tests.base.base_mock import BaseMock
from tests.factory import OrderFactory


class MockOrderManager(BaseMock):
    def __init__(self):
        super().__init__()
        self.init_data = self.init_data()

    def mock_get_orders_by_user(self, user_id: int, order_status: List[int]) -> List[Order]:
        if not order_status:
            return self.init_data
        elif order_status == [OrderStatus.NEW]:
            return [order for order in self.init_data if order.status == OrderStatus.NEW]
        else:
            return []

    def init_data(self) -> List[Order]:
        return [
            OrderFactory.build(id=1, order_uuid="uuid_1231", user_id=1111, status=OrderStatus.NEW),
            OrderFactory.build(id=2, order_uuid="uuid_1232", user_id=1112, status=OrderStatus.NEW),
            OrderFactory.build(id=3, order_uuid="uuid_1232", user_id=1112, status=OrderStatus.COMPLETED)
        ]