#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pytest

from design_pytterns.singleton import Singleton


@pytest.fixture(name='Subclass')
def subclass_definition():
    class MySingletonClass(Singleton):
        def __init__(self, arg, *args, **kwargs):
            self.arg = arg
            self.args = args
            self.kwargs = kwargs

    return MySingletonClass


def test_same_instance(Subclass):
    assert id(Subclass(1, 2)) == id(Subclass(3,4))

def test_no_type_error_raised(Subclass):
    Subclass(1)
    Subclass()
