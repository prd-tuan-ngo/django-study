#! /usr/bin/python
#
# Copyright (C) 2025 paradox.ai
#
# Release: 1.0.0
# @link olivia.paradox.ai
#
__author__ = "tuan.ngo"
__date__ = "19:04"
from typing import TypeVar, Generic

from abc import abstractmethod, ABC

FROM_OBJECT = TypeVar('FROM_OBJECT')
TO_OBJECT = TypeVar('TO_OBJECT')


class IConverter(ABC, Generic[FROM_OBJECT, TO_OBJECT]):
    @abstractmethod
    def convert(self, from_object : FROM_OBJECT) -> TO_OBJECT:
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def convert_list(self, from_objects : [FROM_OBJECT]) -> [TO_OBJECT]:
        raise NotImplementedError("Not implemented yet")


