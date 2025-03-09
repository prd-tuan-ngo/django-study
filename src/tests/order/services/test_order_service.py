#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "16:42"

from unittest.mock import patch

import pytest

from order.constants.order import OrderStatus
from order.domain.getter import OrderGetter
from order.services.order_service import OrderService
from tests.base.base_test import BaseTest
from tests.order.base.stub.order_getter_stub import StubOrderGetter


class BaseOrderServiceTest(BaseTest):
    @pytest.fixture(autouse=True)
    def _setUp(self):
        self.instance_under_test = OrderService

    def _tearDown(self):
        pass

class TestGetOrderByUser(BaseOrderServiceTest):
    @patch.object(OrderGetter, "get_orders_by_user", StubOrderGetter.get_orders_by_user_with_new_status)
    def test_get_order_by_user_with_new_status(self):
        # Arrange
        user_id = 1111
        order_status_filter = [OrderStatus.NEW]

        #Act
        orders = self.instance_under_test.get_orders_by_user(user_id, order_status_filter)

        #Assert
        self.assertEqual(2, len(orders))

        # Tear down
        self._tearDown()


    @patch.object(OrderGetter, "get_orders_by_user", StubOrderGetter.get_orders_by_user_with_all_status)
    def test_get_order_by_user_with_all_status(self):
        # Arrange
        user_id = 1111
        order_status_filter = []

        # Act
        orders = self.instance_under_test.get_orders_by_user(user_id, order_status_filter)

        # Assert
        self.assertEqual(3, len(orders))

        # Tear down
        self._tearDown()
