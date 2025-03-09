#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:43"

from dataclasses import dataclass, field

from order.dataclasses.order.orderdata import OrderData
from order.dataclasses.shipping import ShippingOrderDetails
from order.dataclasses.shop import Shop


@dataclass
class OrderDetailData:
    order : OrderData = field(default_factory=OrderData)
    shipping_order: ShippingOrderDetails  = field(default_factory=ShippingOrderDetails)
    shop: Shop  = field(default_factory=Shop)
    to_address : str = field(default_factory=str)
    cod_amount : int = field(default_factory=int)
