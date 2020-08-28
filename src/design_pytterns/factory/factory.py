#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Generic Factory-pattern."""

import logging
from typing import Any, Hashable, MutableMapping, Optional

from design_pytterns.errors import UnregisteredClassIdError


class Factory():
    """
    Generic Factory-pattern based on hashable id class registration.

    Parameters
    ----------
    registered_classes: dict, optional
        A dictionary that maps the hashable identifiers with their class types.

    """

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
        """
        Register a class by a hashable identifier.

        Parameters
        ----------
        class_id : Hashable
            The class identifer.
        class_type : type
            The class type.

        Warnings
        --------
        Overwrite any previously mapped type if its class id is already in use
        and log a warning about the replacement.

        """
        if class_id in self._registered_classes:
            self.__LOGGER.warning(
                'class id %s is used by %s, replacing it with %s',
                repr(class_id),
                repr(self._registered_classes[class_id]),
                repr(class_type)
            )

        self._registered_classes[class_id] = class_type

    def create(self, class_id: Hashable, *args: Any, **kwargs: Any) -> Any:
        """
        Create a class instance given its identifier and constructor arguments.

        .. versionchanged:: 0.2.0 raises `UnregisteredClassIdError` instead of
            `TypeError`.

        Parameters
        ----------
        class_id : Hashable
            The class identifer.
        *args : Any
            Variable length arguments of the class constructor associated to
            the value of `class_id`.
        **kwargs: Any
            Keyword arguments of class constructor associated to the value of
            `class_id`.

        Returns
        -------
        Any
            Initialized class instance associated to the value of `class_id`.

        Raises
        ------
        UnregisteredClassIdError
            If `class_id` is unknown.

        """
        if class_id in self._registered_classes:
            return self._registered_classes[class_id](*args, **kwargs)

        raise UnregisteredClassIdError(class_id)
