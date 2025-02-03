#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:47"

from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=["GET"], url_path="list-orders", url_name="list-orders")
    def list(self, request):
        pass

    @action(detail=False, methods=["POST"], url_path="create", url_name="create-orders")
    def create(self, request):
        pass