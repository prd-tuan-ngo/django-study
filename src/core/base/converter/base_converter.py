#! /usr/bin/python
#
# Copyright (C) 2024 paradox.ai
#
# Release: 2.4.5
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "19:13"

from abc import abstractmethod
from typing import Generic, TypeVar

from core.base.converter.converter_interface import IConverter

FROM_OBJECT = TypeVar('FROM_OBJECT')
TO_OBJECT = TypeVar('TO_OBJECT')


class BaseConverter(IConverter, Generic[FROM_OBJECT, TO_OBJECT]):
    """
    Base class for all converters
    """

    def convert(self, from_object: FROM_OBJECT) -> TO_OBJECT:
        if from_object :
            return self._convert_hook(from_object)
        exception = self._get_default_exeption()
        if exception:
            raise exception
        return self._get_default_value()

    def convert_list(self, from_objects: [FROM_OBJECT]) -> [TO_OBJECT]:
        if from_objects:
            to_objects = []
            for obj in from_objects:
                to_objects.append(self.convert(obj))
            return to_objects
        exception = self._get_default_exeption()
        if exception:
            raise exception
        return self._get_default_value()

    @abstractmethod
    def _convert_hook(self, from_object: FROM_OBJECT) -> TO_OBJECT:
        raise NotImplementedError("Not implemented yet")

    def _get_default_exeption(self):
        return Exception("Default Exception")

    def _get_default_value(self):
        return None
