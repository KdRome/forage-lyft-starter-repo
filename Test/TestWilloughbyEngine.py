import unittest
from Engine.WilloughbyEngine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 700000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = 50000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
