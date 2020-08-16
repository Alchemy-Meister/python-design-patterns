from collections.abc import Hashable
from inspect import isabstract
import logging
from typing import MutableMapping, Type

from design_pytterns.interfaces import SubclassIdentificable

class ConcreteSubclassRegister():

    __LOGGER = logging.getLogger(__name__)

    def __init__(self, base_class: Type[SubclassIdentificable]) -> None:
        if not issubclass(base_class, SubclassIdentificable):
            raise TypeError(
                f'unidentificable base class: {repr(base_class.__name__)}'
            )

        self.registered_classes = self._register_subclasses(base_class)

    def _register_subclasses(
            self, base_class: Type[SubclassIdentificable]
    ) -> MutableMapping[Hashable, Type[SubclassIdentificable]]:
        registered_classes = {}

        current_class = base_class
        pending_classes = current_class.__subclasses__()

        while pending_classes:
            current_class = pending_classes.pop(0)
            if current_class not in registered_classes.values():
                if not isabstract(current_class):
                    if current_class.CLASS_ID in registered_classes.keys():
                        self.__LOGGER.warning(
                            'class id %s is used by %s, replacing it with %s',
                            repr(current_class.CLASS_ID),
                            repr(registered_classes[current_class.CLASS_ID]),
                            repr(current_class)
                        )

                    registered_classes.update(
                        {current_class.CLASS_ID: current_class}
                    )

                pending_classes = (
                    current_class.__subclasses__() + pending_classes
                )

        return registered_classes
