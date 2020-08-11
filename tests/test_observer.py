#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Any

import pytest

from design_pytterns.observer import EventPublisher, Publisher, Subscriber

@pytest.fixture(name='my_subscriber_class')
def subclass_definition():
    class MySubscriberClass(Subscriber):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.update_call_counter = 0

        def update(self, *args: Any, **kwargs: Any):
            self.args = args
            self.kwargs = kwargs
            self.update_call_counter += 1

    return MySubscriberClass

def test_remove_unknown_subscriber(my_subscriber_class):
    publisher = Publisher()
    unknown_subscriber = my_subscriber_class()

    publisher.unsubscribe(unknown_subscriber)

def test_single_notification_duplicated_subscriber(my_subscriber_class):
    publisher = Publisher()
    subscriber = my_subscriber_class()

    assert subscriber.update_call_counter == 0

    publisher.subscribe(subscriber)
    publisher.subscribe(subscriber)

    publisher.notify()

    assert subscriber.update_call_counter == 1

def test_dont_notify_unsubscriber(my_subscriber_class):
    publisher = Publisher()

    subscriber = my_subscriber_class()
    unsubscriber = my_subscriber_class()

    assert subscriber.update_call_counter == 0
    assert unsubscriber.update_call_counter == 0

    publisher.subscribe(subscriber)
    publisher.subscribe(unsubscriber)

    publisher.notify()

    assert subscriber.update_call_counter == 1
    assert unsubscriber.update_call_counter == 1

    publisher.unsubscribe(unsubscriber)

    publisher.notify()

    assert subscriber.update_call_counter == 2
    assert unsubscriber.update_call_counter == 1

def test_event_publisher(my_subscriber_class):
    publisher = EventPublisher(('start', 'finish',))

    subscriber_1 = my_subscriber_class()
    subscriber_2 = my_subscriber_class(0xDEADBEEF, 'foo', var=(0, 1, 2,))
    subscriber_3 = my_subscriber_class('test')

    assert subscriber_1.update_call_counter == 0
    assert subscriber_2.update_call_counter == 0
    assert subscriber_3.update_call_counter == 0

    publisher.subscribe('start', subscriber_1)
    publisher.subscribe('finish', subscriber_2)
    publisher.subscribe('finish', subscriber_3)

    publisher.notify('start')

    assert subscriber_1.update_call_counter == 1
    assert subscriber_2.update_call_counter == 0
    assert subscriber_3.update_call_counter == 0

    publisher.notify('finish')

    assert subscriber_1.update_call_counter == 1
    assert subscriber_2.update_call_counter == 1
    assert subscriber_3.update_call_counter == 1

    publisher.unsubscribe('finish', subscriber_3)

    publisher.notify('finish')

    assert subscriber_1.update_call_counter == 1
    assert subscriber_2.update_call_counter == 2
    assert subscriber_3.update_call_counter == 1
