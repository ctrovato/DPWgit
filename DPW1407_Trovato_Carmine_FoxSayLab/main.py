'''
Carmine Trovato
July 20th 2014
DPW1407 Fox Say Lab
'''



import webapp2
from fox import Fox
from rabbit import Rabbit
from wolf import Wolf

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #objects made from the subclasses
        f = Fox()
        w = Wolf()
        r = Rabbit()

        #array made from the objects instantiated above
        the_animals = [f, w, r]

        # conditions for the pages to be printed out according to the link clicked
        # defaults to the rabbit page
        if self.request.GET:
            animal = self.request.GET["animal"]
            if animal == "rabbit":
                self.response.write(the_animals[2].print_out())
            elif animal == "wolf":
                self.response.write(the_animals[1].print_out())
            else:
                self.response.write(the_animals[0].print_out())
        else:
            self.response.write(the_animals[2].print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)