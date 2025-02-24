#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "21:59"

from factory.django import DjangoModelFactory

from order.models import OrderDetail


class OrderDetailFactory(DjangoModelFactory):
    class Meta:
        model = OrderDetail