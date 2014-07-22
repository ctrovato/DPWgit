__author__ = 'CarmineTrovato'

class Animal(object):
    def __init__(self):
        self.__css_url = "css/styles.css"
        self.__title1 = "What did the Fox say?"
        self._title = ""
        self._font = "http://fonts.googleapis.com/css?family=Ubuntu+Mono:400italic' rel='stylesheet' type='text/css'"
        self._animal = "The animal"
        self._fox = ""
        self._phylum = ""
        self._class_ = ""
        self._order = ""
        self._family = ""
        self._genus = ""
        self._avg_lifespan = ""
        self._habitat = ""
        self._geo_location = ""
        self.__sound = ""
        self._body_id = ""
        self._link = ""
        self._open = ""
        self._content = ""
        self._close = ""


    @property
    def main_title(self):
        return self.__title1


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title



    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, new_animal):
        if new_animal == "":
            self._animal = self._animal
        else:
            self._animal = new_animal



    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new_sound):
        if new_sound == "":
            self.__sound = self.__sound
        else:
            self.__sound = new_sound


    @property
    def css(self):
        return self.__css_url

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
