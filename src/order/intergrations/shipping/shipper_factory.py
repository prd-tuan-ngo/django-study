# Copyright (C) 2025 paradox.ai
#
# Release: 2.4.9
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "22:10"

from order.constants.shipping_provider import ShippingProvider
from order.intergrations.shipping.ghn.ghn_shipping_adapter import GHNShippingAdapter


class ShippingAdapterFactory:
    SHIPPING_ADAPTERS = {
        ShippingProvider.GHN: GHNShippingAdapter,
    }
    @staticmethod
    def get_shipping_adapter(shipping_Provider: int):
        shipping_provider = ShippingAdapterFactory.SHIPPING_ADAPTERS.get(shipping_Provider)
        if not shipping_provider:
            raise Exception("Shipping provider not found")
        return shipping_provider()
