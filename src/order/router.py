#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:48"

from django.conf import settings
from django.urls import re_path as url, include
from rest_framework import routers

from order.views.order import OrderViewSet

app_name = settings.ORDER
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'order', OrderViewSet, basename="Order")

urlpatterns = [
    url(r'^', include(router.urls)),
]