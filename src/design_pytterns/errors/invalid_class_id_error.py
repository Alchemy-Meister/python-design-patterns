#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Invalid class identifier error."""

from .design_pyttern_error import DesignPytternError


class InvalidClassIdError(DesignPytternError):
    """Raised when the ``CLASS_ID`` of a `SubclassIdentifiable` is `None`."""

    def __init__(self):
        super().__init__(message="invalid subclass identifier: 'None'")
