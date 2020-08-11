#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Any, List

from .subscriber import Subscriber

class Publisher():
    def __init__(self):
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify(self, *args: Any, **kwargs: Any):
        for subscriber in self._subscribers:
            subscriber.update(*args, **kwargs)
