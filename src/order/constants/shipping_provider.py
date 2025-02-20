#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:17"


class ShippingProviderBaseEndPoint:
    GHN = "https://online-gateway.ghn.vn/shiip/public-api/v2/shipping-order"

class GHNShippingProvider:
        CREATE_ORDER = ShippingProviderBaseEndPoint.GHN + "/create"
        GET_ORDER = ShippingProviderBaseEndPoint.GHN + "/detail"