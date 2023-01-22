from Serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.Engine = engine
        self.Battery = battery
    
    def needs_service(self):
        return True
