from abc import ABC, abstractmethod

class IShip(ABC):
    @abstractmethod
    def sail_to(self, destination_port):
        pass

    @abstractmethod
    def refuel(self, amount):
        pass

    @abstractmethod
    def load(self, container):
        pass

    @abstractmethod
    def unload(self, container):
        pass


class Ship(IShip):
    def __init__(self, ship_id, fuel, port, weight_capacity, max_containers, fuel_per_km):
        self.id = ship_id
        self.fuel = fuel
        self.current_port = port
        self.weight_capacity = weight_capacity
        self.max_containers = max_containers
        self.fuel_per_km = fuel_per_km
        self.containers = []

    def sail_to(self, destination_port):
        distance = self.current_port.get_distance(destination_port)
        fuel_needed = distance * self.fuel_per_km + sum(c.consumption() for c in self.containers)
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            self.current_port.outgoing_ship(self)
            destination_port.incoming_ship(self)
            self.current_port = destination_port
            return True
        return False

    def refuel(self, amount):
        self.fuel += amount

    def load(self, container):
        if len(self.containers) < self.max_containers:
            self.containers.append(container)
            return True
        return False

    def unload(self, container):
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False
