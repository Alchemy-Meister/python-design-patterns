#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from pytest import raises

from design_pytterns.interfaces import SubclassIdentificable

def test_base_class_with_class_id():
    class Father(SubclassIdentificable, class_id=0xABC):
        pass

    assert Father.CLASS_ID == 0xABC

def test_base_class_none_class_id():
    class Father(SubclassIdentificable):
        pass

    assert Father.CLASS_ID is None

def test_multiple_inheritance():
    class Father(SubclassIdentificable):
        pass

    class Mother():
        pass

    class Son(Father, Mother, class_id='me'):
        pass

    class GrandSon(Son, class_id='my_son'):
        pass

    assert Son.CLASS_ID == 'me'
    assert GrandSon.CLASS_ID == 'my_son'

def test_subclass_invalid_none_identifier_value():
    class Father(SubclassIdentificable):
        pass

    with raises(ValueError):
        class Son(Father):
            pass

def test_base_unhashable_identifier():
    with raises(TypeError):
        class Father(SubclassIdentificable, class_id={'is_dad': True}):
            pass

def test_subclass_unhashable_identifier():
    class Father(SubclassIdentificable):
        pass

    class Mother():
        pass

    with raises(TypeError):
        class Son(Father, Mother, class_id=['dad', 'mom']):
            pass