#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Generic Subscriber-pattern."""

from abc import ABC, abstractmethod
from typing import Any


class Subscriber(ABC):
    """Abstract subscriber. Define the generic ``update`` method."""

    @abstractmethod
    def update(self, *args: Any, **kwargs: Any):
        """
        Abstract update method.

        Parameters
        ----------
        *args : Any
            Variable length arguments.
        **kwargs : Any
            Arbitrary keyword arguments.

        """
