#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Unhashable class identifier error."""

from typing import Any

from .design_pyttern_error import DesignPytternError


class UnhashableClassIdError(DesignPytternError):
    """
    Raised when the ``CLASS_ID`` of a `SubclassIdentifiable` is not hashable.

    Parameters
    ----------
    class_id : Any
        Unhashable value that raised the exception.

    """

    def __init__(self, class_id: Any):
        super().__init__(
            message=f'unhashable type: {type(class_id).__name__}'
        )
