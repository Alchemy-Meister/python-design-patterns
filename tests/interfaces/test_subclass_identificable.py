#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from pytest import raises

from design_pytterns.interfaces import SubclassIdentifiable


def test_base_class_with_class_id():
    class Father(SubclassIdentifiable, class_id=0xABC):
        pass

    assert Father.CLASS_ID == 0xABC


def test_base_class_none_class_id():
    class Father(SubclassIdentifiable):
        pass

    assert Father.CLASS_ID is None


def test_multiple_inheritance():
    class Father(SubclassIdentifiable):
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
    class Father(SubclassIdentifiable):
        pass

    with raises(ValueError):
        class _Son(Father):
            pass


def test_base_unhashable_identifier():
    with raises(TypeError):
        class _Father(SubclassIdentifiable, class_id={'is_dad': True}):
            pass


def test_subclass_unhashable_identifier():
    class Father(SubclassIdentifiable):
        pass

    class Mother():
        pass

    with raises(TypeError):
        class _Son(Father, Mother, class_id=['dad', 'mom']):
            pass
