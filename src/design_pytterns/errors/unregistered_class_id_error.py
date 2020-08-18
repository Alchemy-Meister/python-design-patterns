#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from collections.abc import Hashable

from .design_pyttern_error import DesignPytternError

class UnregisteredClassIdError(DesignPytternError):
    def __init__(self, class_id: Hashable) -> None:
        super().__init__(
            class_id, message=f'unregistered class id: {repr(class_id)}'
        )
