import unittest
from ship import Ship
from port import Port
from container import BasicContainer

class TestShip(unittest.TestCase):
    def setUp(self):
        self.port1 = Port(port_id=1, latitude=40.0, longitude=50.0)
        self.port2 = Port(port_id=2, latitude=41.0, longitude=51.0)
        self.ship = Ship(ship_id=1, fuel=1000, port=self.port1, weight_capacity=10000, max_containers=10, fuel_per_km=5)

    def test_sail_to_success(self):
        self.ship.fuel = 2000  # достатньо палива
        self.assertTrue(self.ship.sail_to(self.port2))
        self.assertEqual(self.ship.current_port, self.port2)

    def test_sail_to_fail(self):
        self.ship.fuel = 10  # недостатньо палива
        self.assertFalse(self.ship.sail_to(self.port2))
        self.assertEqual(self.ship.current_port, self.port1)

    def test_load_container(self):
        container = BasicContainer(container_id=1, weight=2000)
        self.assertTrue(self.ship.load(container))
        self.assertIn(container, self.ship.containers)

    def test_unload_container(self):
        container = BasicContainer(container_id=1, weight=2000)
        self.ship.load(container)
        self.assertTrue(self.ship.unload(container))
        self.assertNotIn(container, self.ship.containers)

if __name__ == '__main__':
    unittest.main()
