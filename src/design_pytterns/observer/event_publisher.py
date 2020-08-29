#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Generic Event Publisher-pattern."""

from typing import Any, Hashable, Sequence

from .publisher import Publisher
from .subscriber import Subscriber


class EventPublisher():
    """
    Event based Publisher-pattern.

    Parameters
    ----------
    events: Sequence
        The sequence that contains all the possible hashable events

    """

    def __init__(self, events: Sequence[Hashable]):
        self._publishers = {event: Publisher() for event in events}

    def subscribe(self, event: Hashable, subscriber: Subscriber):
        """
        Register a new subscriber for an event.

        If the subscriber instance is already registered for the event the
        subscription is discarded.

        Parameters
        ----------
        event: Hashable
            The event which the subscriber registers to.
        subscriber : Subscriber
            The subscriber instance to register.

        """
        self._publishers[event].subscribe(subscriber)

    def unsubscribe(self, event: Hashable, subscriber: Subscriber):
        """
        Deregister the subscriber from an event.

        If the subscriber instance is unknown for the given event, the
        unsubscription is discarded.

        Parameters
        ----------
        event: Hashable
            The event which the subscriber deregister from.
        subscriber : Subscriber
            The subscriber instance to deregister.

        """
        self._publishers[event].unsubscribe(subscriber)

    def notify(self, event: Hashable, *args: Any, **kwargs: Any):
        """
        Execute the ``update`` method of all the event subscribers.

        Parameters
        ----------
        event : Hashable
            The event which all its subscribers are notified.
        *args : Any
            Variable length contextual arguments.
        **kwargs : Any
            Contextual keyword arguments.

        """
        self._publishers[event].notify(*args, **kwargs)
