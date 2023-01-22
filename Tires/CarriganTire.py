from Tires.Tires import Tires

class CarriganTires(Tires):
    def __init__(self, TireWear):
        self.TireWear = TireWear

    def needs_service(self):
        for Tire in self.TireWear:
            if Tire >= 0.9:
                return True
        return False