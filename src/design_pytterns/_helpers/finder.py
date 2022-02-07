#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2021-2022 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""scan_module Class Finder."""

from __future__ import annotations

from collections.abc import Iterator
from importlib import import_module
from inspect import getmembers, isclass
from itertools import chain
from pkgutil import walk_packages, iter_modules
from types import ModuleType


class Finder():
    """Container class for class finder operations."""

    @staticmethod
    def module_classes(
        scan_module: ModuleType,
        scan_submodules: bool = True,
        public_only: bool = True
    ):
        """
        Retrieve all the classes of a given module.

        If the provided module is a package, iterate over all its modules and
        extract their classes.

        Parameters
        ----------
        scan_module: ModuleType
            The module to be scanned.
        scan_submodules: bool
            If True, the default, process all the module levels. Else process
            only the root level.
        public_only: bool
            If true (the default), scan only public classes within public
            modules. Else include also privates.

        Returns
        -------
        Iterator[tuple[str, type]]
            An an iterator of tuples containing the qualified name and type of
            each found class.

        """
        try:
            package_path: str = scan_module.__path__
            if scan_submodules:
                search_function = walk_packages
            else:
                search_function = iter_modules

            return chain(
                Finder._get_classes(scan_module, public_only),
                *(
                    Finder._get_classes(import_module(name), public_only)
                    for _, name, _ in search_function(
                        package_path, f'{scan_module.__name__}.'
                    )
                )
            )

        except AttributeError:
            return Finder._get_classes(scan_module, public_only)

    @staticmethod
    def _class_filter(
        class_name: str, cls: type, module: ModuleType, public_only: bool
    ) -> bool:
        if public_only:
            return (
                not class_name.startswith('_')
                and cls.__module__ == module.__name__
            )

        return cls.__module__ == module.__name__

    @staticmethod
    def _get_classes(
        module: ModuleType, public_only: bool
    ) -> Iterator[tuple[str, type]]:
        if not public_only or Finder._is_module_public(module.__name__):
            yield from (
                (f'{module.__name__}.{class_name}', class_type)
                for class_name, class_type in getmembers(module, isclass)
                if Finder._class_filter(
                    class_name, class_type, module, public_only
                )
            )

        yield from ()

    @staticmethod
    def _is_module_public(module_name: str) -> bool:
        try:
            module_name = module_name.rsplit('.')[1]
        except IndexError:
            pass

        if module_name.startswith('_'):
            return False

        return True
