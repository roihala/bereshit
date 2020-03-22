from abc import ABCMeta, abstractmethod


class Base(ABCMeta):
    @abstractmethod
    def run(cls):
        pass
