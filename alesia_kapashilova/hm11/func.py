from abc import ABC, abstractmethod


class Methods(ABC):

    @abstractmethod
    def sum(self, a, b):
        pass

    @abstractmethod
    def dif(self, a, b):
        pass

    @abstractmethod
    def mul(self, a, b):
        pass

    @abstractmethod
    def div(self, a, b):
        pass
