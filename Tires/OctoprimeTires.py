from Tires.Tires import Tires

class OctoprimeTire(Tires):
    def __init__(self, TireWear):
        self.TireWear = TireWear

    def needs_service(self):
        TireWearSum = sum(self.TireWear) >= 3
        return TireWearSum