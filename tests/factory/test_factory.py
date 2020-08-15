#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

from pytest import fixture

from design_pytterns.factory import Factory

@fixture(name='test_class')
def test_class_definition():
    class Test():
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    return Test

def test_contructor_registration(test_class):
    my_factory = Factory({'test': test_class})

    args = (1, 2, 3,)
    kwargs = {'foo': 'bar'}

    test_instance = my_factory.create('test', *args, **kwargs)

    assert test_instance.args == args
    assert test_instance.kwargs == kwargs

def test_manual_class_registration(test_class):
    my_factory = Factory()
    my_factory.register_class('test', test_class)

    args = (1, 2, 3,)
    kwargs = {'foo': 'bar'}

    test_instance = my_factory.create('test', *args, **kwargs)

    assert test_instance.args == args
    assert test_instance.kwargs == kwargs

def test_id_already_in_use_warning(caplog, test_class):
    my_factory = Factory({'test': test_class})
    my_factory.register_class('test', test_class)

    assert len(caplog.records) == 1

    record = next(iter(caplog.records))

    assert record.levelno == logging.WARNING
