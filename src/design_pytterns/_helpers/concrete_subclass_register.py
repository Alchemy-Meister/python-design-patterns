#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Concrete Subclass Register."""

from collections.abc import Hashable
from inspect import isabstract
import logging
from typing import MutableMapping, Type

from design_pytterns.errors import UnidentifiableSubclassError
from design_pytterns.interfaces import SubclassIdentifiable


class ConcreteSubclassRegister():
    """
    Concrete subclass register.

    Analyze the subclass hierarchy of the given base class that
    inherits from `SubclassIdentifiable` and registers all of the concrete
    subclasses with their associated class id automatically.

    Parameters
    ----------
    base_class: Type[SubclassIdentifiable]
        The base class that servers as the starting point of the subclass
        hierarchy analysis.

    Raises
    ------
    UnidentifiableSubclassError
        If `base_class` does not inherit from SubclassIdentifiable.

    .. versionchanged:: 0.3.0 raises `UnidentifiableSubclassError` instead of
            `TypeError`.

    """

    __LOGGER = logging.getLogger(__name__)

    def __init__(self, base_class: Type[SubclassIdentifiable]) -> None:
        if not issubclass(base_class, SubclassIdentifiable):
            raise UnidentifiableSubclassError(base_class)

        self.registered_classes = self._register_subclasses(base_class)

    def _register_subclasses(
            self, base_class: Type[SubclassIdentifiable]
    ) -> MutableMapping[Hashable, Type[SubclassIdentifiable]]:
        registered_classes = {}

        current_class = base_class
        pending_classes = current_class.__subclasses__()

        while pending_classes:
            current_class = pending_classes.pop(0)
            if current_class not in registered_classes.values():
                if not isabstract(current_class):
                    if current_class.CLASS_ID in registered_classes.keys():
                        self.__LOGGER.warning(
                            'class id %s is used by %s, replacing it with %s',
                            repr(current_class.CLASS_ID),
                            repr(registered_classes[current_class.CLASS_ID]),
                            repr(current_class)
                        )

                    registered_classes.update(
                        {current_class.CLASS_ID: current_class}
                    )

                pending_classes = (
                    current_class.__subclasses__() + pending_classes
                )

        return registered_classes
