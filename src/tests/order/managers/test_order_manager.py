#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "20:52"

from order.constants.order import OrderStatus
from order.models import Order, OrderDetail, Product
from tests.base.base_manager_test import BaseManagerTest
from tests.factory import OrderFactory, OrderDetailFactory, ProductFactory


class BaseOrderManagerTest(BaseManagerTest):
    def setUp(self):
        self.product_1 = ProductFactory(name="product_1", price=1000, description="description_1")
        self.product_2 = ProductFactory(name="product_2", price=2000, description="description_2")

        self.order_1_new = OrderFactory(order_uuid="uuid_1231", user_id=1111, status=OrderStatus.NEW)
        self.order_2_new = OrderFactory(order_uuid="uuid_1232", user_id=1112, status=OrderStatus.NEW)
        self.order_3_canceled = OrderFactory(order_uuid="uuid_1233", user_id=1111, status=OrderStatus.CANCELLED)
        self.order_4_refunded = OrderFactory(order_uuid="uuid_1234", user_id=1111, status=OrderStatus.REFUNDED)

        self.order_detail_1 = OrderDetailFactory(order_id=self.order_1_new.id, product_id=self.product_1.id, quantity=1, price=1000, total=1000)
        self.order_detail_2 = OrderDetailFactory(order_id=self.order_2_new.id, product_id=self.product_2.id, quantity=2, price=4000, total=8000)
        self.order_detail_3 = OrderDetailFactory(order_id=self.order_3_canceled.id, product_id=self.product_2.id, quantity=1, price=2000, total=2000)

    def tearDown(self):
        OrderDetail.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()

class TestGetOrderDetails(BaseOrderManagerTest):
    def test_get_order_details_when_order_exiting_with_new_status(self):
        # Arrange
        self.setUp()

        # Act
        order = Order.objects.get_order_details(self.order_1_new.id)
        order_detail = order.order_detail.first()

        # Assert
        self.assertEqual(order.order_uuid, "uuid_1231")
        self.assertEqual(str(order.status), str(OrderStatus.NEW))
        self.assertEqual(order_detail.price, 1000)

        # Teardown
        self.tearDown()

    def test_get_order_details_when_order_exiting_with_canceled_status(self):
        # Arrange
        self.setUp()

        # Act
        order = Order.objects.get_order_details(self.order_3_canceled.id)
        order_detail = order.order_detail.first()

        # Assert
        self.assertEqual(order.order_uuid, "uuid_1233")
        self.assertEqual(str(order.status), str(OrderStatus.CANCELLED))
        self.assertEqual(order_detail.price, 2000)

        # Teardown
        self.tearDown()

    def test_get_order_details_when_order_not_exiting(self):
        # Arrange
        self.setUp()

        # Act
        not_exist_order_id = 9999999999
        order = Order.objects.get_order_details(not_exist_order_id)

        # Assert
        self.assertIsNone(order)

        # Teardown
        self.tearDown()