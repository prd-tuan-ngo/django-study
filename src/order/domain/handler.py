#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:29"

from typing import Dict

from core.base.base_handler import BaseHandler
from order.dataclasses.order import Order
from order.domain.actions.create_order import CreateOrderAction


class OrderHandler(BaseHandler):
    def __init__(self):
        pass

    def create_order(self, order_data: Dict) -> Order:
        """
        Create order
        """
        order = CreateOrderAction().create_order(order_data)
        return order

    def send_mail_order_created(self, user_id: int, order: Order):
        # TODO send mail after order created.
        pass

