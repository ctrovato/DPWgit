
__author__ = 'CarmineTrovato'


from animals import Animal
from html import Html

class Wolf(Animal, Html):
    def __init__(self):
        #constructor function
        Animal.__init__(self)
        Html.__init__(self)
        self.title = "The Grey Wolf"
        self.animal = "GREY WOLF"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Carnivora"
        self._family = "Canidae"
        self._genus = "	Canis"
        self._url = "http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wolf%2C_voor_de_natuur%2C_Saxifraga_-_Jan_Nijendijk.5097.jpg/1014px-Wolf%2C_voor_de_natuur%2C_Saxifraga_-_Jan_Nijendijk.5097.jpg"
        self._fox = ""
        self._avg_lifespan = "Five years "
        self._habitat = "Deserts, grasslands, forests and arctic."
        self._geo_location = "North America and Europe, Australia"
        self.sound = "Howl"
        self._body_id = "wolf"
        self._link = "wikimedia.com"

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())