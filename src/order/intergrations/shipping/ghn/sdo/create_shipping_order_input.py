#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:32"

from dataclasses import dataclass


@dataclass
class GHNCreateShippingOderInput:
    token: str
    shop_id: str
    to_name: str
    to_address: str
    from_name: str = ""
    weight: float = 0
    length: float = 0
    width: float = 0
    height: float = 0
    cod_amount: float = 0