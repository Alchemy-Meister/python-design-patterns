#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Generic package error."""

from typing import Any


class DesignPytternError(Exception):
    """
    Base class for all design_patterns exceptions.

    Parameters
    ----------
    *args : Any
        Variable length arguments.
    **kwargs : Any
        Arbitrary keyword arguments.

    Attributes
    ----------
    message : str
        A descriptive sentence explaining the error.

    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.message = kwargs.pop('message', '')

        super().__init__(*args, **kwargs)
