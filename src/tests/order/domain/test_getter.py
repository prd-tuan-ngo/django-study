#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "16:49"
from unittest.mock import patch

from order.constants.order import OrderStatus
from order.domain.getter import OrderGetter
from tests.base.base_test import BaseTest
from tests.order.base.mock.order_manager_mock import OrderManagerMock


class BaseGetterTest(BaseTest):
    def setUp(self):
        self.instance_under_test = OrderGetter
        pass

    def tearDown(self):
        pass

class TestGetOrderByUser(BaseGetterTest):
    @patch('order.managers.orders.OrdersManager.get_orders_by_user')
    def test_get_order_by_user_with_no_status_filter_and_return_list_orders(self, order_manager_mock):
        # Arrange
        self.setUp()
        user_id = 1111
        order_status_filter = []
        order_manager_mock.side_effect = OrderManagerMock().mock_get_orders_by_user

        #Act
        orders = self.instance_under_test.get_orders_by_user(user_id, order_status_filter)

        #Assert
        self.assertEqual(len(orders), 3)

        #Teardown
        self.tearDown()

    @patch('order.domain.getter.OrderGetter.get_orders_by_user')
    def test_get_order_by_user_with_status_filter_new_and_return_list_orders(self, order_getter_mock):
        pass


    def test_get_order_by_user_with_status_filter_cancel_and_return_no_order(self):
        pass
