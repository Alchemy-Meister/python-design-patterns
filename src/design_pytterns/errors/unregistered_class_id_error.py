#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Unregistered class id error."""

from collections.abc import Hashable

from .design_pyttern_error import DesignPytternError


class UnregisteredClassIdError(DesignPytternError):
    """
    Raised when a factory creates an instance of an unknown class id.

    Parameters
    ----------
    class_id : Hashable
        Unknown hashable that raised the exception.

    """

    def __init__(self, class_id: Hashable) -> None:
        super().__init__(
            class_id, message=f'unregistered class id: {repr(class_id)}'
        )
