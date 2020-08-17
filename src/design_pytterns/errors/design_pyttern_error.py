#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Any

class DesignPytternError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.message = kwargs.pop('message', '')

        super().__init__(*args, **kwargs)
