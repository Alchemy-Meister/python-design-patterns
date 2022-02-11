#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020-2022 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Subclass Factory."""

from __future__ import annotations

import logging
from types import ModuleType
from typing import Optional

from design_pytterns._helpers import ConcreteSubclassRegistrant, Finder
from design_pytterns.interfaces import SubclassIdentifiable

from .factory import Factory


class SubclassFactory(Factory):
    """
    Automatic concrete sublass registration factory.

    Factory that analyzes the subclass hierarchy of the given `base_class` that
    inherits from `SubclassIdentifiable` and registers all of the concrete
    subclasses with their associated class id automatically at runtime.

    .. versionchanged:: 0.7.0 Added ``subclass_module``, ``scan_submodules``
        and ``public_only`` optional arguments. Log a warning if no subclasses
        are found.

    Parameters
    ----------
    base_class: SubclassIdentifiable
        The base class that servers as the starting point of the subclass
        hierarchy analysis.
    subclass_module: Optional[ModuleType]
        Module containing all the subclasses of the base class. If provided,
        scan the module and automatically import the classes definied within.
        If the module is a package, iterate over all its modules.
    scan_submodules: bool
        When ``subclass_module`` is provided, and if true (the default),
        process all the module levels. Else process only the root level.
    public_only: bool
        When ``subclass_module`` is provided, and if true (the default), scan
        only public classes within public modules. Else include also privates.

    Warnings
    --------
    For the subclass analysis to work, all subclasses must be imported before
    hand, either manually or alternatively using the ``subclass_module``
    argument to automatically import them at runtime. If no subclasses are
    found log a warning message.

    """

    __LOGGER = logging.getLogger(__name__)

    def __init__(
        self,
        base_class: type[SubclassIdentifiable],
        subclass_module: Optional[ModuleType] = None,
        scan_submodules: bool = True,
        public_only: bool = True
    ) -> None:
        if subclass_module:
            subclass_context = Finder().module_classes(
                subclass_module, scan_submodules, public_only
            )

        else:
            subclass_context = None

        super().__init__(
            ConcreteSubclassRegistrant(
                base_class, subclass_context
            ).registered_classes
        )
        if not self._registered_classes:
            self.__LOGGER.warning(
                'empty factory: %s, base class %s does not have any '
                'subclasses registered. Possible import missing, use the '
                'subclass_module argument to add them automatically',
                self.__class__.__name__,
                base_class.__qualname__
            )
