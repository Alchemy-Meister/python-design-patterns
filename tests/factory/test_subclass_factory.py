#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from abc import ABC, abstractmethod
import logging
from pytest import fixture, raises

from design_pytterns.factory import SubclassFactory
from design_pytterns.errors import UnregisteredClassIdError
from design_pytterns.interfaces import SubclassIdentificable


@fixture(name='class_hierarchy_dict')
def class_hierarchy():
    class MyBaseClass(SubclassIdentificable):
        pass

    class Class1(MyBaseClass, class_id=1):
        pass

    class Class2(MyBaseClass, class_id=2):
        pass

    class Class3(MyBaseClass, class_id=3):
        pass

    class Class4(Class1, Class2, class_id=4):
        pass

    class Class5(Class1, class_id=5):
        pass

    class Class6(Class2, Class3, class_id=6):
        pass

    class Class7(Class2, ABC, class_id=7):
        @abstractmethod
        def test(self):
            pass

    class Class8(Class7, class_id=8):
        def test(self):
            return 'test'

    return {
        'base': MyBaseClass,
        'class1': Class1,
        'class2': Class2,
        'class3': Class3,
        'class4': Class4,
        'class5': Class5,
        'class6': Class6,
        'class7': Class7,
        'class8': Class8
    }


def test_automatic_concrete_class_registration(class_hierarchy_dict):
    my_subclass_factory = SubclassFactory(class_hierarchy_dict['base'])

    for index in range(1, 7):
        assert isinstance(
            my_subclass_factory.create(index),
            class_hierarchy_dict[f'class{index}']
        )

    assert isinstance(
        my_subclass_factory.create(8), class_hierarchy_dict['class8']
    )


def test_abstract_class_omitted(class_hierarchy_dict):
    my_subclass_factory = SubclassFactory(class_hierarchy_dict['base'])
    with raises(UnregisteredClassIdError):
        my_subclass_factory.create(7)


def test_unidentificable_base_class():
    class MyUnidentificableBaseClass():
        pass

    class _UnidentificableClass1(MyUnidentificableBaseClass):
        pass

    with raises(TypeError):
        SubclassFactory(MyUnidentificableBaseClass)


def test_repeated_class_id_warning(caplog, class_hierarchy_dict):
    class Class9(class_hierarchy_dict['class8'], class_id=1):
        pass

    my_subclass_factory = SubclassFactory(class_hierarchy_dict['base'])

    assert isinstance(my_subclass_factory.create(1), Class9)
    assert len(caplog.records) == 1

    record = next(iter(caplog.records))

    assert record.levelno == logging.WARNING
