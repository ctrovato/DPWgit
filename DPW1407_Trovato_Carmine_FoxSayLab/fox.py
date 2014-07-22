__author__ = 'CarmineTrovato'

from animals import Animal
from html import Html

class Fox(Animal, Html):
    def __init__(self):
        #call constructor functions
        Animal.__init__(self)
        Html.__init__(self)
        #the property below is just a test to make sure my main stylesheet was protected
        self.__css_url = ""

        self.title = "The Fox"
        self.animal = "FOX"
        self._phylum = "Chordata"
        self._class_ = "Mammalia"
        self._order = "Carnivora"
        self.__family = "Canidae"
        self._genus = "Vulpes"
        self._url = "images/fox-4.png"
        self._fox = "images/megan_fox.jpeg"
        self._avg_lifespan = "Five years"
        self._habitat = "Woodlands"
        self._geo_location = "North America"
        self.sound = "howl"
        self._body_id = "fox"
        self._link = "flickr.com"

    #this is the polymorphic function. It updates the html for every different animal and
    # overwrites the following super class functions: title(), animal(), and sound()
    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())