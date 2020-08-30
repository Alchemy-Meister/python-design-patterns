#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Unidentifiable subclass error."""

from .design_pyttern_error import DesignPytternError


class UnidentifiableSubclassError(DesignPytternError):
    """
    Raised when the base class of a subclass register is not identifiable.

    Parameters
    ----------
    base_class : type
        Unidentifiable type that raised the exception.

    """

    def __init__(self, base_class: type):
        super().__init__(
            message=f'unidentifiable base class: {repr(base_class.__name__)}'
        )
