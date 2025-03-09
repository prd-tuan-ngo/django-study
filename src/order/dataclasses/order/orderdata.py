#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:24"

from dataclasses import dataclass, field


@dataclass
class OrderData:
    id : int = field(default_factory=int)
    order_uuid : str = field(default_factory=str)
    user_id : int = field(default_factory=int)
    shipping_order_uuid : str = field(default_factory=str)
    status : int = field(default_factory=int)