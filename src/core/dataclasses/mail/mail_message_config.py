#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "14:17"

from dataclasses import dataclass


@dataclass
class MailMessageConfig:
    from_email: str
    to: list
    cc: list
    bcc: list
    message: str
