#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:47"


from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from order.services.order_service import OrderService


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=["GET"], url_path="list-orders", url_name="list-orders")
    def list(self, request):
        """
        @apiVersion 1.0.0
        @api {GET} /list Get the list of orders
        @apiName ListOrders
        @apiGroup JobDistribution
        @apiParam {json} data The data to save the attribute settings
            {}
        """
        try:
            request_params = request.query_params.copy()
            user_id = request_params.get("user_id")
            order_status = request_params.get("order_status")
            orders = OrderService.get_orders_by_user(user_id, order_status)
            return Response(orders, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["POST"], url_path="create", url_name="create-orders")
    def create(self, request):
        pass