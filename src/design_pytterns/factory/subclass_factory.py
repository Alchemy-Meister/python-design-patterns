#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Type

from design_pytterns._helpers import ConcreteSubclassRegister
from design_pytterns.interfaces import SubclassIdentificable

from .factory import Factory

class SubclassFactory(Factory):
    def __init__(self, base_class: Type[SubclassIdentificable]):
        super().__init__(
            ConcreteSubclassRegister(base_class).registered_classes
        )
