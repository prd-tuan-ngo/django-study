#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:35"

from dataclasses import dataclass


@dataclass
class GHNGetShippingOrderInput:
    token: str
    order_code: str