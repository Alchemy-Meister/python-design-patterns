#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Singleton metaclass."""

from typing import Any, Dict, Tuple


class SingletonMeta(type):
    """Metaclass implementation of Singleton-pattern."""

    def __init__(
            cls, name: str, bases: Tuple[type, ...], mmbs: Dict[str, Any]
    ) -> None:
        super().__init__(name, bases, mmbs)
        cls._instance = None

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Invoke ``__call__`` method only if global instance is `None`."""
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
