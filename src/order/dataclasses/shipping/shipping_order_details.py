#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:11"

from dataclasses import dataclass, field


@dataclass
class ShippingOrderDetails:
    shipping_order_uuid: str = field(default_factory=str)
    is_cod: bool = field(default_factory=bool)
    log: list = field(default_factory=list)