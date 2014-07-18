# Carmine Trovato
#07/17/2014
# Quiz 2

#Racer Nationality

import webapp2
from american import American
from english import English

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write
        a = American()
        print a.print_out()

        e = English()
        print e.print_out()

        content = a.print_out() + e.print_out()

        self.response.write(a.print_out())
        self.response.write(e.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

