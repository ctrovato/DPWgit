from racers import Racers

class American(Racers):
    def __init__(self):
        Racers.__init__(self)
        self._name = "Carmine Trovato"
        self._age = 10
        self._brand = "Subaru"
        self._speed = 120
        self._class = "Rally"
        self._titles = "5 X Champion"


def update(self):
        self.all = "</br>" + "Racer Name: " + self._name + "</br>Racer Age: " + str(self._age) + \
                   "</br>Racer Brand: " + self._brand + "</br>Racer Speed: " + str(self._speed) + "km/h" +\
                   "</br>Racer Class: " + self._class + \
                   "</br>" + self._titles + "</br>"