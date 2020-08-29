#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Package with implementations of Singleton-pattern."""

from .singleton import Singleton
from .singleton_meta import SingletonMeta

__all__ = ['Singleton', 'SingletonMeta']
