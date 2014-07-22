
__author__ = 'CarmineTrovato'


from animals import Animal
from html import HTML

class Wolf(Animal, HTML):
    def __init__(self):
        #constructor function
        Animal.__init__(self)
        HTML.__init__(self)
        self.title = "The Grey Wolf"
        self.animal = "GREY WOLF"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Carnivora"
        self._family = "Canidae"
        self._genus = "	Canis"
        self._url = "images/GreyWolf.jpg"
        self._avg_lifespan = "Five years "
        self._habitat = "Deserts, Woodlands and Arctic."
        self._geo_location = "North America and Europe, Australia"
        self.sound = "Howling"
        self._body_id = "wolf"

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())