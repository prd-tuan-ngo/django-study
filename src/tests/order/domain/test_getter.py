#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "16:49"
from unittest.mock import patch

import pytest

from order.constants.order import OrderStatus
from order.domain.getter import OrderGetter
from tests.base.base_test import BaseTest
from tests.order.base.mock.order_manager_mock import MockOrderManager


class BaseGetterTest(BaseTest):
    @pytest.fixture(autouse=True)
    def _setUp(self):
        self.instance_under_test = OrderGetter

    def _tearDown(self):
        pass

class TestGetOrderByUser(BaseGetterTest):
    @patch('order.managers.orders.OrdersManager.get_orders_by_user')
    def test_get_order_by_user_with_no_status_filter_and_return_list_orders(self, order_manager_mock):
        # Arrange
        user_id = 1111
        order_status_filter = []
        order_manager_mock.side_effect = MockOrderManager().mock_get_orders_by_user

        #Act
        orders = self.instance_under_test.get_orders_by_user(user_id, order_status_filter)

        #Assert
        self.assertEqual(len(orders), 3)
        # Check number of call. It will be useful in case we want to check how many times the method is called
        order_manager_mock.assert_called_once_with(user_id, order_status_filter)

        # Tear down
        self._tearDown()

    @patch('order.domain.getter.OrderGetter.get_orders_by_user')
    def test_get_order_by_user_with_status_filter_new_and_return_list_orders(self, order_getter_mock):
        pass


    def test_get_order_by_user_with_status_filter_cancel_and_return_no_order(self):
        pass
