from Engine.Engine import Engine

class CapuletEngine(Engine):
    def __init__(self, engine, battery, last_service_mileage, current_mileage):
        super().__init__(engine, battery)
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self):
        if (self.current_mileage - self.last_service_mileage) > 30000:
            return True
        else:  
            return False