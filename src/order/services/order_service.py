#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:06"

from typing import List, Dict

from core.base.base_service import BaseService
from core.domain.mail.mail_service import MailService
from core.utils.function import safe_executor
from order.constants.order import OrderStatus
from order.dataclasses.order import OrderData
from order.domain.getter import OrderGetter
from order.domain.handler import OrderHandler


class OrderService(BaseService):
    handler = OrderHandler
    getter = OrderGetter

    @classmethod
    @safe_executor(with_log=True, re_raise=True)
    def create_order(cls, order: Dict) -> OrderData:
        """
        Create order
        """
        user_id = super().get_user().user_id
        if order := cls.handler.create_order(user_id, order):
            cls.handler.send_mail_order_created(user_id, order)
            return order
        raise Exception("Failed to create order")

    @classmethod
    def get_orders_by_user(cls, user_id: int, order_status: List[int]) -> List[OrderData]:
        """
        Get orders by user_id and order_status
        """
        if not user_id:
            user_id = super().get_user().user_id
        return cls.getter.get_orders_by_user(user_id, order_status)

    @classmethod
    def get_order_details(cls, order_id):
        """
        Get order details by order_id
        """
        order = cls.getter.get_order_details(order_id)
        if not order:
            raise Exception("Order not found")


