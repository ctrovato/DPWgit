__author__ = 'CarmineTrovato'

from animals import Animal
from html import Html

class Rabbit(Animal, Html):
    def __init__(self):
        #constructor function
        Animal.__init__(self)
        Html.__init__(self)
        self.title = "The Rabbit"
        self.animal = "Rabbit"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Lagomorpha"
        self._family = "Leporidae"
        self._genus = "Sylvilagus"
        self._url = "images/Rabbit.jpg"
        self._avg_lifespan = "Ten years"
        self._habitat = "Woodlands, Meadows, Forests."
        self._geo_location = "North, South America, Asia, Europe, Africa, Australia"
        self.sound = "Weening"
        self._body_id = "rabbit"
        self._link = "wikimedia.com"


    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())
