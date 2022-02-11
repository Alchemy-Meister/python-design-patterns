#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020-2022 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Implementation of SubclassIdentifiable interface-like class."""

from collections.abc import Hashable
from inspect import isabstract

from design_pytterns.errors import InvalidClassIdError, UnhashableClassIdError


class SubclassIdentifiable():
    """
    Inject ``class_id`` class attribute to all concrete subclasses of the base.

    The concrete subclasses of the base that inherits from this class require
    the ``class_id`` keyword argument in the class definition with a `Hashable`
    not `None` value.

    .. versionchanged:: 0.7.0
        - allow abstract classes to be unidentifiable.
        - renamed `CLASS_ID` to `class_id`, as class attribute is not constant.

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
    >>> MyIdentifiableSubclass.class_id
    1

    """

    class_id: Hashable = None

    def __init_subclass__(cls, class_id: Hashable = None) -> None:
        if not isabstract(cls):
            if not isinstance(class_id, Hashable):
                raise UnhashableClassIdError(class_id)

            if SubclassIdentifiable not in cls.__bases__ and class_id is None:
                raise InvalidClassIdError()

            cls.class_id = class_id
