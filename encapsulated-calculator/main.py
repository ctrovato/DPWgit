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
#====== sony obj=====
        sony = Television()
        sony.television = 'Sony BRAVIA 52" LED HDTV'
        sony.price = 3199.99
        sony.sound = 999.99
        sony.bluray = 160
        sony.warranty = 229.99
        sony.final_tax = (sony.price + sony.sound + sony.bluray + sony.warranty)
        sony.total = sony.price + sony.sound + sony.bluray + sony.warranty

#====== lg obj======
        lg = Television()
        lg.television = 'LG 48" LED HDTV'
        lg.price = 2999.99
        lg.sound = 1049.99
        lg.bluray = 159.99
        lg.warranty = 179.99
        lg.final_tax = (lg.price + lg.sound + lg.bluray + lg.warranty)
        lg.total = lg.price + lg.sound + lg.bluray + lg.warranty

#====== vizio obj======
        vizio = Television()
        vizio.television = 'VIZIO M-Series 42" LED HDTV'
        vizio.price = 2299.99
        vizio.sound = 1099.99
        vizio.bluray = 159.99
        vizio.warranty = 229.99
        vizio.final_tax = (vizio.price + vizio.sound + vizio.bluray + vizio.warranty)
        vizio.total = vizio.price + vizio.sound + vizio.bluray + vizio.warranty

#====== insignia obj=====
        insignia = Television()
        insignia.television = 'Insignia 42" LED HDTV'
        insignia.price = 1999.99
        insignia.sound = 1199.99
        insignia.bluray = 129.99
        insignia.warranty = 219.99
        insignia.final_tax = (insignia.price + insignia.sound + insignia.bluray + insignia.warranty)
        insignia.total = insignia.price + insignia.sound + insignia.bluray + insignia.warranty

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)