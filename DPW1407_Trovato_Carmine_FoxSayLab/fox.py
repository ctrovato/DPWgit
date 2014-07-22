__author__ = 'CarmineTrovato'

from animals import Animal
from html import HTML

class Fox(Animal, HTML):
    def __init__(self):
        #constructor functions
        Animal.__init__(self)
        HTML.__init__(self)

        self.__css_url = ""

        self.title = "The Fox"
        self.animal = "Red Fox"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Carnivora"
        self.__family = "Canidae"
        self._genus = "Vulpes"
        self._url = "images/foximg.jpg"
        self._avg_lifespan = "Five years"
        self._habitat = "Woodlands"
        self._geo_location = "North America, Asia, Europe Australia"
        self.sound = "Howling"
        self._body_id = "fox"


    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())