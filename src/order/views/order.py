#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "15:47"

from rest_framework import viewsets, status
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
            {
                "user_id": 1,
                "order_status": ["NEW"]
            }
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
            "order_data": {
                "order_details": [
                    {
                        "product_id": p1,
                        "quantity": 1,
                        "price": 1000
                    }
                ]
            }
            "shipping_data": {
                "shipping_provider": 1,
                "shop_id": shop_1111
            }
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
