#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020-2022 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Concrete Subclass Register."""

from __future__ import annotations

from collections import deque
from collections.abc import Hashable, Iterable
from inspect import isabstract
import logging
from typing import Any, Dict, Optional

from design_pytterns.errors import UnidentifiableSubclassError
from design_pytterns.interfaces import SubclassIdentifiable


class ConcreteSubclassRegistrant():
    """
    Concrete subclass register.

    Analyze the subclass hierarchy of the given base class that
    inherits from `SubclassIdentifiable` and register all of the concrete
    subclasses with their associated class id automatically by traversing
    the tree structure in preorder fashion.

    .. versionchanged:: 0.7.0
      - Renamed class to ConcreteSubclassRegistrant
      - Added ``subclass_context`` argument.

    .. versionchanged:: 0.3.0 Raises `UnidentifiableSubclassError` instead of
        `TypeError`.

    Parameters
    ----------
    base_class: Type[SubclassIdentifiable]
        The base class that servers as the starting point of the subclass
        hierarchy analysis.

    Raises
    ------
    UnidentifiableSubclassError
        If `base_class` does not inherit from SubclassIdentifiable.

    Warns
    -----
    Overwrite any previously registered type if duplicated `class_id` is found
        and log a warning about the replacement.

    """

    __LOGGER = logging.getLogger(__name__)

    def __init__(
        self,
        base_class: type[SubclassIdentifiable],
        subclass_context: Optional[Iterable[tuple[str, Any]]] = None

    ) -> None:
        if not issubclass(base_class, SubclassIdentifiable):
            raise UnidentifiableSubclassError(base_class) from None

        if subclass_context:
            locals().update(subclass_context)

        self.registered_classes = self._register_subclasses(base_class)

    def _register_subclasses(
            self, base_class: type[SubclassIdentifiable]
    ) -> Dict[Hashable, type[SubclassIdentifiable]]:
        registered_classes: Dict[Hashable, type[SubclassIdentifiable]] = {}

        current_class = base_class
        pending_classes = deque(current_class.__subclasses__())

        while pending_classes:
            current_class = pending_classes.popleft()
            if current_class not in registered_classes.values():
                if not isabstract(current_class):
                    class_id = current_class.class_id
                    if class_id in registered_classes:
                        self.__LOGGER.warning(
                            'class id %r is used by %r, replacing it with %r',
                            class_id,
                            registered_classes[class_id],
                            current_class
                        )

                    registered_classes.update({class_id: current_class})

                pending_classes.extendleft(
                    reversed(current_class.__subclasses__())
                )

        return registered_classes
