#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:08"

from dataclasses import dataclass, field


@dataclass
class ShippingOrder:
    order_uuid: str = field(default_factory=str)
    shipping_order_uuid: str = field(default_factory=str)
    client_id: str = field(default_factory=str)
    provider: int = field(default_factory=int)
    status: int = field(default_factory=int)