#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Implementation of SubclassIdentifiable interface-like class."""

from collections.abc import Hashable
from typing import Any, Optional

from design_pytterns.errors import InvalidClassIdError, UnhashableClassIdError


class SubclassIdentifiable():
    """
    Inject ``CLASS_ID`` class attribute to all the subclasses of the base.

    The subclasses of the base that inherits from this class require the
    ``class_id`` keyword argument in the class definition with a `Hashable` not
    `None` value.

    .. versionchanged:: 0.4.0

        - raise `UnhashableClassIdError` instead of `TypeError`.
        - raise `InvalidClassIdError` instead of `ValueError`.

    Raises
    ------
    UnhashableClassIdError
        If `class_id` is not `Hashable`.
    InvalidClassIdError
        If `class_id` is None for any of the subclasses.

    Examples
    --------
    >>> from design_pytterns.interfaces import SubclassIdentifiable
    >>>
    >>> class MyBase(SubclassIdentifiable):
    ...    pass
    ...
    >>> class MyIdentifiableSubclass(MyBase, class_id=1):
    ...    pass
    ...
    >>> MyIdentifiableSubclass.CLASS_ID
    1

    """

    def __init_subclass__(
            cls, class_id: Optional[Hashable] = None, **kwargs: Any
    ) -> None:
        super().__init_subclass__(**kwargs)

        if not isinstance(class_id, Hashable):
            raise UnhashableClassIdError(class_id)

        if SubclassIdentifiable.mro()[0] not in cls.__bases__:
            if class_id is None:
                raise InvalidClassIdError()

        cls.CLASS_ID = class_id
