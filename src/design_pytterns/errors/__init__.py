#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Subpackage with the exception definitions."""

from .design_pyttern_error import DesignPytternError
from .invalid_class_id_error import InvalidClassIdError
from .unhashable_class_id_error import UnhashableClassIdError
from .unidentifiable_subclass_error import UnidentifiableSubclassError
from .unregistered_class_id_error import UnregisteredClassIdError

__all__ = [
    'DesignPytternError',
    'InvalidClassIdError',
    'UnhashableClassIdError',
    'UnidentifiableSubclassError',
    'UnregisteredClassIdError'
]
