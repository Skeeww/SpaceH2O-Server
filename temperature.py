import json
from sensors import Sensor

class Temperature(Sensor):
    def __init__(self):
        self.json = None
        with open("sensors/temperature.json", "r") as file:
            self.json = json.load(file)
        self.name = self.json['name']
        self.units = self.json['units']
        self.refreshRate = self.json['refreshRate']