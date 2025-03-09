# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "22:15"

from unittest.mock import patch

import pytest

from order.constants.order import OrderStatus
from order.dataclasses.shipping import ShippingOrder
from order.domain.actions.create_order import CreateOrderAction
from order.intergrations.shipping.shipper_factory import ShippingAdapterFactory
from order.models import Order
from tests.base.base_test import BaseTest
from tests.order.base.fake.shipping_adapter_fake import FakeShippingAdapter


class BaseCreateOrderActionTest(BaseTest):
    @pytest.fixture(autouse=True)
    def _setUp(self):
        self.instance_under_test = CreateOrderAction()
        self.shipping_data_input: dict = {
            "order_data": {
                "order_details": [
                    {
                        "product_id": "1",
                        "quantity": 1,
                        "price": 1000
                    }
                ]
            },
            "shipping_data": {
                "shipping_provider": 1,
                "shop_id": 1111,
                "to_address": "1234 address",
                "cod_amount": 1000
            }
        }

    def _tearDown(self):
        pass

class TestCreateOrderActionWithMockShippingService(BaseCreateOrderActionTest):

    @patch('order.intergrations.shipping.ghn.ghn_shipping_adapter.GHNShippingAdapter.create_shipping_order')
    @patch('order.managers.orders.OrdersManager.create')
    def test_create_order_with_mock_manager_and_shipping_service_successful(self, order_manager_mock, shipping_provider_mock):
        # Arrange
        order_manager_mock.return_value = Order(id=1111, order_uuid="1234_1111", user_id=1122, status=OrderStatus.NEW)
        shipping_provider_mock.return_value = ShippingOrder(order_uuid="1234_1111", shipping_order_uuid="ghn_1234_1111")


        # Act
        order_data = self.instance_under_test.create_order(1122, self.shipping_data_input)

        # Assert
        self.assertEqual(1111, order_data.id)
        self.assertEqual(1, shipping_provider_mock.call_count)

        # Tear down
        self._tearDown()


class TestCreateOrderActionWithFakeShippingService(BaseCreateOrderActionTest):
    @patch('order.intergrations.shipping.shipper_factory.ShippingAdapterFactory.get_shipping_adapter')
    @patch('order.managers.orders.OrdersManager.create')
    def test_create_order_with_mock_manager_and_fake_shipping_service_successful(self, order_manager_mock, shipping_factory_mock):
        # Arrange
        order_manager_mock.return_value = Order(id=1111, order_uuid="1234_1111", user_id=1122, status=OrderStatus.NEW)
        shipping_factory_mock.return_value = FakeShippingAdapter()

        # Act
        order_data = self.instance_under_test.create_order(1122, self.shipping_data_input)

        # Assert
        self.assertEqual(1111, order_data.id)
        self.assertEqual(1, shipping_factory_mock.call_count)

        # TODO verify fake shipping order is created
        shipping_provider: int = self.shipping_data_input.get("shipping_data").get("shipping_provider")
        shipping_order = ShippingAdapterFactory.get_shipping_adapter(shipping_provider).get_shipping_order(
            order_data.shipping_order_uuid)
        self.assertEqual(order_data.shipping_order_uuid, shipping_order.shipping_order_uuid)

        # Tear down
        self._tearDown()



