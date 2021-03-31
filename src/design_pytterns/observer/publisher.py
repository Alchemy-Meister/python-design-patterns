#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020-2021 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Generic Publisher-pattern."""

from __future__ import annotations

from typing import Any

from .subscriber import Subscriber


class Publisher():
    """Generic Publisher-pattern."""

    def __init__(self) -> None:
        self._subscribers: list[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        """
        Register a new subscriber.

        If the subscriber instance is already registered the subscription is
        discarded.

        Parameters
        ----------
        subscriber : Subscriber
            The subscriber instance to register.

        """
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        """
        Deregister the subscriber.

        If the subscriber instance is unknown, the unsubscription is discarded.

        Parameters
        ----------
        subscriber : Subscriber
            The subscriber instance to deregister.

        """
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify(self, *args: Any, **kwargs: Any) -> None:
        """
        Execute the ``update`` method of all the registered subscribers.

        Parameters
        ----------
        *args : Any
            Variable length contextual arguments.
        **kwargs : Any
            Contextual keyword arguments.

        """
        for subscriber in self._subscribers:
            subscriber.update(*args, **kwargs)
