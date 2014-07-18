class Racers(object):
    def __init__(self):
        self.__title = "Racers Profile"
        self._name = ""
        self._brand = ""
        self._speed = 0
        self._class = ""



    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.__title + "</br>" + "Racer Name: " + self._name +"</br>Racer Brand: " + self._brand +\
                   "</br>Racer Speed: " + str(self._speed) + "km/h" + "</br>Racer Class: " + self._class + \
                   "</br>Racer age: " + str(self._age)+ "</br> </br>"