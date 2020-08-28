#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Generic Singleton-pattern."""

from .singleton_meta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    """
    Class implementation of Singleton-pattern.

    This implementation of the Singleton pattern calls the ``__init__``
    method of the subclass once, for the initialization of the global
    instance. In the following calls to the constructor, the ``__init__``
    method is not executed, ignoring any argument passed to it and returning
    the very first created instance instead.

    Examples
    --------
    >>> from design_pytterns.singleton import Singleton
    >>>
    >>> class MyNumber(Singleton):
    ...     def __init__(self, number):
    ...         self.number = number
    ...     def __str__(self):
    ...         return self.number
    ...
    >>> test_1 = MyNumber(5)
    >>> test_2 = MyNumber()  # No TypeError is raised
    >>> test_3 = MyNumber(10)
    >>>
    >>> id(test_1), test_1
    (139703749013216, 5)
    >>> id(test_2), test_2
    (139703749013216, 5)
    >>> id(test_3), test_3
    (139703749013216, 5)

    """
