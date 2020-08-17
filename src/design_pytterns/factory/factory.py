#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
from typing import Any, Hashable, MutableMapping, Optional

from design_pytterns.errors import UnregisteredClassIdError

class Factory():

    __LOGGER = logging.getLogger(__name__)

    def __init__(
            self,
            registered_classes: Optional[MutableMapping[Hashable, type]] = None
    ) -> None:
        if registered_classes is None:
            self._registered_classes = {}
        else:
            self._registered_classes = registered_classes

    def register_class(self, class_id: Hashable, class_type: type) -> None:
        if class_id in self._registered_classes:
            self.__LOGGER.warning(
                'class id %s is used by %s, replacing it with %s',
                repr(class_id),
                repr(self._registered_classes[class_id]),
                repr(class_type)
            )

        self._registered_classes[class_id] = class_type

    def create(self, class_id: Hashable, *args: Any, **kwargs: Any) -> Any:
        if class_id in self._registered_classes:
            return self._registered_classes[class_id](*args, **kwargs)

        raise UnregisteredClassIdError(class_id)
