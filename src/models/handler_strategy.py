from abc import ABC, abstractmethod


class HandlerStrategy(ABC):

    @abstractmethod
    def execute(self):
        pass
