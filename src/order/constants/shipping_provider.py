#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "23:17"

class ShippingProvider:
    GHN = 1
    GHTK = 2
    VIETTEL_POST = 3
    VN_POST = 4


class ShippingProviderBaseEndPoint:
    GHN = "https://online-gateway.ghn.vn/shiip/public-api/v2/shipping-order"

class GHNShippingProvider:
        CREATE_ORDER = ShippingProviderBaseEndPoint.GHN + "/create"
        GET_ORDER = ShippingProviderBaseEndPoint.GHN + "/detail"