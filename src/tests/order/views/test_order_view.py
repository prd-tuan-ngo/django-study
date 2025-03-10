# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "22:12"

from unittest.mock import patch

import pytest
from rest_framework import status

from rest_framework.test import APIClient

from order.services.order_service import OrderService
from tests.base.base_test import BaseTest
from tests.base.base_viewset_test import BaseViewSetTest
from tests.order.base.stub.order_service_stub import StubOrderService


class BaseOrderViewSetTest(BaseViewSetTest):
    @pytest.fixture(autouse=True)
    def _setUp(self):
        self.instance_under_test = APIClient()

    def _tearDown(self):
        pass

class TestListOrders(BaseOrderViewSetTest):
    @pytest.fixture(autouse=True)
    def _setUpInternal(self):
        self.base_url = "/api/v1/order/list-orders"

    @patch.object(OrderService, "get_orders_by_user", StubOrderService.get_orders_by_user_with_new_status)
    def test_list_orders_with_new_status_and_return_success(self):
        # Act
        response = self.instance_under_test.get(path=self.base_url, data={"user_id": 0, "order_status": ["NEW"]})

        # Assert
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # Tear down
        self._tearDown()

    @patch.object(OrderService, "get_orders_by_user", StubOrderService.get_orders_with_raise_exception)
    def test_list_orders_with_new_status_and_return_exception(self):
        # Act
        response = self.instance_under_test.get(path=self.base_url, data={"user_id": 0, "order_status": ["NEW"]})

        # Assert
        self.assertEqual(status.HTTP_500_INTERNAL_SERVER_ERROR, response.status_code)

        # Tear down
        self._tearDown()