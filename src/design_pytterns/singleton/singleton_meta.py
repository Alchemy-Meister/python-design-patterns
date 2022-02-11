#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020-2022 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Singleton metaclass."""

from typing import Any


class SingletonMeta(type):
    """Metaclass implementation of Singleton-pattern."""

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        try:
            return cls._instance
        except AttributeError:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
