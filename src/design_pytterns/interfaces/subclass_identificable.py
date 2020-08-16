#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from collections.abc import Hashable
from typing import Any, Optional

class SubclassIdentificable():
    def __init_subclass__(
            cls, class_id: Optional[Hashable] = None, **kwargs: Any
    ) -> None:
        super().__init_subclass__(**kwargs)

        if not isinstance(class_id, Hashable):
            raise TypeError(f'unhashable type: {type(class_id).__name__}')

        if SubclassIdentificable.mro()[0] not in cls.__bases__:
            if class_id is None:
                raise ValueError("invalid subclass identifier: 'None'")

        cls.CLASS_ID = class_id
