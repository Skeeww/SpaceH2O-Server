class Sensor:
    def __init__(self, name, units, refreshRate):
        self.name = name
        self.units = units
        self.refreshRate = refreshRate
    def getName(self):
        return self.name
    def getUnits(self):
        return self.units
    def getRefreshRate(self):
        return self.refreshRate
    def setName(self, name):
        self.name = name
    def setUnits(self, units):
        self.units = units
    def setRefreshRate(self, refreshRate):
        self.refreshRate = refreshRate
