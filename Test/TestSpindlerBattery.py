import unittest
from datetime import datetime
from Battery.SpindlerBattery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):

    # Testing to see if battery needs_service is true
    def test_needs_service(self):
        #setting current date to todays date
        current_date = datetime.fromisoformat("2023-01-21")
        #setting last service date to more than 2 years back
        last_service_date = datetime.fromisoformat("2013-01-21")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    # Testing to see if battery needs_service is false
    def test_doesnt_need_service(self):   
        #setting current date to todays date
        current_date = datetime.fromisoformat("2023-01-21")
        #setting last service date to less than 2 years back
        last_service_date = datetime.fromisoformat("2022-01-21")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())