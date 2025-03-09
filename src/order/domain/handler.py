#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:29"

from typing import Dict

from core.base.base_handler import BaseHandler
from order.dataclasses.order import OrderData
from order.domain.actions.create_order import CreateOrderAction


class OrderHandler(BaseHandler):
    def __init__(self):
        pass

    @classmethod
    def create_order(cls, user_id: int, order_data: Dict) -> OrderData:
        """
        Create order
        """
        order = CreateOrderAction().create_order(user_id, order_data)
        return order

    @classmethod
    def send_mail_order_created(cls, user_id: int, order: OrderData):
        # TODO send mail after order created.
        pass

