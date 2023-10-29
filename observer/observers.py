from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(mode=None):
        pass


class SubjectObservers:
    def __init__(self, listObservers=[]) -> None:
        self.listObservers: list = listObservers
        self.listSongs = []

    # attach
    def addObserver(self, observer):
        self.listObservers.append(observer)

    # desattach
    def removeObserver(self, observer):
        self.listObservers.remove(observer)

    def notifyAllObservers(self, mode=None):
        for o in self.listObservers:
            o.update(mode if mode is not None else None)
