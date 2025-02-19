#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:06"

from dataclasses import dataclass, field


@dataclass
class Shop:
    shop_uuid: str = field(default_factory=str)
    name: int = field(default_factory=int)
    address: str = field(default_factory=str)
    status: int = field(default_factory=int)