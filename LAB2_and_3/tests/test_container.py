import unittest
from container import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer

class TestContainer(unittest.TestCase):
    def test_basic_container_consumption(self):
        container = BasicContainer(container_id=1, weight=2000)
        self.assertEqual(container.consumption(), 5000)

    def test_heavy_container_consumption(self):
        container = HeavyContainer(container_id=2, weight=4000)
        self.assertEqual(container.consumption(), 12000)

    def test_refrigerated_container_consumption(self):
        container = RefrigeratedContainer(container_id=3, weight=3000)
        self.assertEqual(container.consumption(), 15000)

    def test_liquid_container_consumption(self):
        container = LiquidContainer(container_id=4, weight=2500)
        self.assertEqual(container.consumption(), 10000)

if __name__ == '__main__':
    unittest.main()
