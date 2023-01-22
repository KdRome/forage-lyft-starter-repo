from Car import Car

class Engine(Car):

    def __init__(self, engine, battery):
        super().__init__(engine, battery)

    def needs_service(self):
        pass