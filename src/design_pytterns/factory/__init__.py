#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Package with implementations of Factory-patterns."""

from .factory import Factory
from .subclass_factory import SubclassFactory

__all__ = ['Factory', 'SubclassFactory']
