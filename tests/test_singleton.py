#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pytest

from design_pytterns.singleton import Singleton

@pytest.fixture(name='Subclass')
def subclass_definition():
    class MySingletonClass(Singleton):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    return MySingletonClass

def test_same_instance(Subclass):
    a_singleton = Subclass(1, 2)
    b_singleton = Subclass(3, 4)
    c_singleton = Subclass()

    assert dir(a_singleton) == dir(b_singleton) == dir(c_singleton)
    assert a_singleton == b_singleton == c_singleton
