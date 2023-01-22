import unittest
from Engine.CapuletEngine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 40000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_doesnt_needs_service(self):
        current_mileage = 20000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())