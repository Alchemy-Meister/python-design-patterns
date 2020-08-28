#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Subclass Factory."""

from typing import Type

from design_pytterns._helpers import ConcreteSubclassRegister
from design_pytterns.interfaces import SubclassIdentifiable

from .factory import Factory


class SubclassFactory(Factory):
    """
    Automatic concrete sublass registration factory.

    Factory that analyzes the subclass hierarchy of the given base class that
    inherits from `SubclassIdentifiable` and registers all of the concrete
    subclasses with their associated class id automatically.

    Parameters
    ----------
    base_class: SubclassIdentifiable
        The base class that servers as the starting point of the subclass
        hierarchy analysis.

    """

    def __init__(self, base_class: Type[SubclassIdentifiable]):
        super().__init__(
            ConcreteSubclassRegister(base_class).registered_classes
        )
