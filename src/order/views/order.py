#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:47"

from dataclasses import asdict

from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from core.constants.http import HttpMethod
from order.serializers.order_serializer import OrderSerializer
from order.services.order_service import OrderService


class OrderViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=[HttpMethod.GET], url_path="list-orders")
    def list_orders(self, request):
        """
        @apiVersion 1.0.0
        @api {GET} /list Get the list of orders
        @apiName ListOrders
        @apiGroup Order
        @apiParam {json}
            {}
        """
        try:
            request_params = request.query_params.copy()
            user_id = request_params.get("user_id")
            order_status = request_params.get("order_status") or []
            orders = OrderService.get_orders_by_user(user_id, order_status)
            order_serialized = OrderSerializer(orders, many=True)
            resp = dict(
                orders=order_serialized.data
            )
            return Response(resp, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=[HttpMethod.POST], url_path="create")
    def create_order(self, request):
        """
        @apiVersion 1.0.0
        @api {POST} /create-orders create order
        @apiName CreateOrder
        @apiGroup Order
        @apiParam {json} data The data to save the order
            {}
        """
        try:
            order = request.data
            order = OrderService.create_order(order)
            order_serialized = OrderSerializer(order)
            resp = dict(
                order=order_serialized.data
            )
            return Response(resp, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
