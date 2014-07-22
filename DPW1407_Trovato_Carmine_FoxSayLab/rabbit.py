__author__ = 'CarmineTrovato'

from animals import Animal
from html import HTML

class Rabbit(Animal, HTML):
    def __init__(self):
        #constructor function
        Animal.__init__(self)
        HTML.__init__(self)
        self.title = "The Rabbit"
        self.animal = "Belgian Hare Rabbit"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Lagomorpha"
        self._family = "Leporidae"
        self._genus = "Sylvilagus"
        self._url = "images/Rabbit.jpg"
        self._avg_lifespan = "Ten years"
        self._habitat = "Woodlands, Prairies, Deserts."
        self._geo_location = "North, South America, Asia, Europe, Africa, Australia"
        self.sound = "Weening"
        self._body_id = "rabbit"


    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())
