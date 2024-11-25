from abc import ABC, abstractmethod

class Container(ABC):
    def __init__(self, container_id, weight):
        self.id = container_id
        self.weight = weight

    @abstractmethod
    def consumption(self):
        pass

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.weight == other.weight
            and isinstance(self, type(other))
        )


class BasicContainer(Container):
    def consumption(self):
        return self.weight * 2.5


class HeavyContainer(Container):
    def consumption(self):
        return self.weight * 3.0


class RefrigeratedContainer(HeavyContainer):
    def consumption(self):
        return self.weight * 5.0


class LiquidContainer(HeavyContainer):
    def consumption(self):
        return self.weight * 4.0
