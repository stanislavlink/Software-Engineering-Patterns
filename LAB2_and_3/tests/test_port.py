import unittest
from port import Port
from ship import Ship

class TestPort(unittest.TestCase):
    def setUp(self):
        self.port1 = Port(port_id=1, latitude=40.0, longitude=50.0)
        self.port2 = Port(port_id=2, latitude=41.0, longitude=51.0)

    def test_incoming_ship(self):
        ship = Ship(ship_id=1, fuel=1000, port=self.port1, weight_capacity=10000, max_containers=10, fuel_per_km=5)
        self.port1.incoming_ship(ship)
        self.assertIn(ship, self.port1.current_ships)
        self.assertIn(ship, self.port1.history)

    def test_outgoing_ship(self):
        ship = Ship(ship_id=1, fuel=1000, port=self.port1, weight_capacity=10000, max_containers=10, fuel_per_km=5)
        self.port1.incoming_ship(ship)
        self.port1.outgoing_ship(ship)
        self.assertNotIn(ship, self.port1.current_ships)

    def test_distance_calculation(self):
        distance = self.port1.get_distance(self.port2)
        self.assertAlmostEqual(distance, 1.414, places=3)

if __name__ == '__main__':
    unittest.main()
