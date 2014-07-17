'''
Carmine Trovato
July 15th 2014
DPW 1407 Encapsulated Calculator
'''


import webapp2
from pages import Television

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')


#====== samsung obj======
        samsung = Television()
        samsung.television = 'Samsung 48" LED HDTV'
        samsung.price = 2999.99
        samsung.sound = 999.99
        samsung.bluray = 149.99
        samsung.warranty = 229.99
        samsung.final_tax = (samsung.price + samsung.sound + samsung.bluray + samsung.warranty)
        samsung.total = samsung.price + samsung.sound + samsung.bluray + samsung.warranty


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)