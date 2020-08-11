#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from abc import ABC, abstractmethod
from typing import Any

class Subscriber(ABC):
    @abstractmethod
    def update(self, *args: Any, **kwargs: Any):
        """ TODO add docstring """
