#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Any, Hashable, Sequence

from .publisher import Publisher
from .subscriber import Subscriber

class EventPublisher():
    def __init__(self, events: Sequence[Hashable]):
        self._publishers = {event: Publisher() for event in events}

    def subscribe(self, event: Hashable, subscriber: Subscriber):
        self._publishers[event].subscribe(subscriber)

    def unsubscribe(self, event: Hashable, subscriber: Subscriber):
        self._publishers[event].unsubscribe(subscriber)

    def notify(self, event: Hashable, *args: Any, **kwargs: Any):
        self._publishers[event].notify(*args, **kwargs)
