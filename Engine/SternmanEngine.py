from Engine.Engine import Engine

class SternmanEngine(Engine):
    def __init__(self, engine, battery, warning_light_is_on):
        super().__init__(engine, battery)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
