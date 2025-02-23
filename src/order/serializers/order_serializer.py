#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "17:08"

from rest_framework import serializers

from core.serializers.base_serializer import BaseSerializer
from order.models import Order


class OrderSerializer(BaseSerializer):
    order_uuid = serializers.CharField()
    user_id = serializers.IntegerField()
    status = serializers.IntegerField()

    class Meta:
        model = Order
        fields = "__all__"