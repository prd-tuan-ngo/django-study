#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "20:39"

from dataclasses import dataclass, field


@dataclass
class User:
    user_id: int = field(default_factory=int)
    name: str = field(default_factory=str)