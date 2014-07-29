
import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #p = Page()
        f = FormPage()
        f.inputs =[{'type' : 'text', 'placeholder':'Zip Code', 'name': 'zip'},
                {'type': 'submit', 'name':'submit','value':'Get Weather'}]
        # if there is stuff in the url, do stuff
        if self.request.GET:
            zip = self.request.GET['zip']

            wm = WeatherModel(zip)  #instance of weather model
            #wm.dos
            wv = WeatherView()
            wv.dos = wm.dos   #this passes the data from the model to the view

            #pass subviiew to the form
            f.additional_view = wv.content
        self.response.write(f.print_out())


class WeatherView(object):
    def __init__(self):
        self.__dos = []
        self.content = ""

    @property
    def dos(self):
        pass

    @dos.setter
    def dos(self, arr):
        self.__dos = arr
        self.create_display()

    def create_display(self):
        for do in self.__dos:
            self.content += "Day:" + do.day
            self.content += " (" + do.date + ')'
            self.content +=" High: " + do.high + " Low: " + do.low
            self.content += "<img src=\"images/" + do.code + '.png" />'
            self.content += "<br />"
        print self.content




class WeatherModel(object):
    """ This is the model class that sending to  request to thr yahoo api and getting the XML """
    def __init__(self, z):
        self.url = "http://xml.weather.yahoo.com/forecastrss?p="

        #creates a request to send to server
        request = urllib2.Request(self.url+z)
        opener = urllib2.build_opener()
        self.data = opener.open(request)
        self.parse()

    def parse(self):
        xmldoc = minidom.parse(self.data)
        forecast = xmldoc.getElementsByTagName("yweather:forecast")

        self.__dos = []
        for item in forecast:
            do = WeatherDataObject()
            do.day = item.attributes['day'].value
            do.date = item.attributes['date'].value
            do.high = item.attributes['high'].value
            do.low = item.attributes['low'].value
            do.code = item.attributes['code'].value
            do.description = item.attributes['text'].value
            #this adds the finished data objects into the array
            self.__dos.append(do)


    @property
    def dos(self):
        return self.__dos



class WeatherDataObject(object):
    """this class is just a big associtive array for holding  the info we need """
    def __init__(self):
        self.high = 0
        self.low = 0
        self.code = 0
        self.description = ""
        self.date =  ""
        self.day = ""




class Page(object):

    _head = """<!DOCTYPE HTML>
<head>
    <title></title>
</head>
<body>"""
    _content = ''
    _close = """
</body>
</html>"""

    def __init__(self):
        pass

    def print_out(self):
        return self._head + self._content + self._close



class FormPage(Page):
    __inputs = []
    _form_open = "<form method=\"GET\" action=""  />"
    _form_close = "</form>"
    additional_view = ""


    def __init__(self):
        #invoke constructor in superclass
        Page.__init__(self)

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, i):
        self.__inputs = i

    def create_inputs(self):
        tot_inputs = ''
        for i in self.__inputs:
            #for each item in out __inputs array
            tot_inputs += '<input type="'+i['type']+ '" name="'+i['name']+'" '
            if 'placeholder' in i:
                tot_inputs += 'placeholder="' + i['placeholder'] + '"'
            if 'value' in i:
                tot_inputs += ' value="'+i['value']+'"'
            tot_inputs += ' />'
        return tot_inputs

#This function overides the print function
    def print_out(self):
        return self._head + self._form_open + self.create_inputs() + self._form_close + self.additional_view + self._close

        #accept an array of dictionaries
        #use it to build





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
