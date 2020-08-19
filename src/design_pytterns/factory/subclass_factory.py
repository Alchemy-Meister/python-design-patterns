#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Subclass Factory."""

from typing import Type

from design_pytterns._helpers import ConcreteSubclassRegister
from design_pytterns.interfaces import SubclassIdentificable

from .factory import Factory


class SubclassFactory(Factory):
    """
    Automatic concrete sublass registration factory.

    Factory that analizes the subclass hierarchy of the given base class that
    inherits from `SubclassIdentificable` and registers all of the concrete
    subclasses with their associated class id automatically.

    Parameters
    ----------
    base_class: SubclassIdentificable
        The base class that servers as the starting point of the subclass
        hierarchy analysis.
    """

    def __init__(self, base_class: Type[SubclassIdentificable]):
        super().__init__(
            ConcreteSubclassRegister(base_class).registered_classes
        )
