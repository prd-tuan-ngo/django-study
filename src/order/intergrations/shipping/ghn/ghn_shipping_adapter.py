#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:15"

import json
from dataclasses import asdict
from http import HTTPStatus
from logging import Logger

import requests
from django.conf import settings

from order.constants.shipping_provider import GHNShippingProvider
from order.dataclasses.order.order_details import OrderDetailData
from order.dataclasses.shipping import ShippingOrder, ShippingOrderDetails
from order.intergrations.shipping.base_shipping_adapter import IShippingAdapter
from order.intergrations.shipping.ghn.sdo.create_shipping_order_input import GHNCreateShippingOderInput
from src.order.intergrations.shipping.ghn.sdo.get_shipping_order_input import GHNGetShippingOrderInput


class GHNShippingAdapter(IShippingAdapter):
    def create_shipping_order(self, order_detail: OrderDetailData) -> ShippingOrder:
        try:
            create_shipping_order_input = GHNCreateShippingOderInput(
                token = settings.GHN_CLIENT_TOKEN,
                shop_id = order_detail.shop.shop_uuid,
                to_name = order_detail.to_address,
                to_address = order_detail.to_address,
            )
            resp = requests.post(GHNShippingProvider.CREATE_ORDER, asdict(create_shipping_order_input))
            if resp.status_code != HTTPStatus.OK:
                Logger.error(f"Error when create shipping order: {resp.text}")
                raise Exception(f"Error when create shipping order: {resp.text}")
            shipping_order = json.loads(resp.json())
            return ShippingOrder(
                order_uuid=shipping_order.get("order_uuid"),
                shipping_order_uuid=shipping_order.get("order_code"),
            )
        except Exception as e:
            Logger.error(f"Error when create shipping order: {e}")
            raise e

    def get_shipping_order(self, shipping_order_uuid: str) -> ShippingOrderDetails:
        get_shipping_order = GHNGetShippingOrderInput(
            token = settings.GHN_CLIENT_TOKEN,
            order_code = shipping_order_uuid,
        )
        resp = requests.get(GHNShippingProvider.GET_ORDER, asdict(get_shipping_order))
        if resp.status_code != HTTPStatus.OK:
            Logger.error(f"Error when get shipping order: {resp.text}")
            raise Exception(f"Error when get shipping order: {resp.text}")
        shipping_order = json.loads(resp.json())
        return ShippingOrderDetails(
            shipping_order_uuid=shipping_order.get("order_code"),
            log=shipping_order.get("log"),
        )