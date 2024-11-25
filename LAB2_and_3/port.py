from abc import ABC, abstractmethod
import math

class IPort(ABC):
    @abstractmethod
    def incoming_ship(self, ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship):
        pass


class Port(IPort):
    def __init__(self, port_id, latitude, longitude):
        self.id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.current_ships = []
        self.history = []

    def incoming_ship(self, ship):
        if ship not in self.current_ships:
            self.current_ships.append(ship)
        if ship not in self.history:
            self.history.append(ship)

    def outgoing_ship(self, ship):
        if ship in self.current_ships:
            self.current_ships.remove(ship)

    def get_distance(self, other_port):
        return math.sqrt(
            (self.latitude - other_port.latitude) ** 2
            + (self.longitude - other_port.longitude) ** 2
        )
