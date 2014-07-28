
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

            #load in info from the api

            #build request - format the official request
            request = urllib2.Request("http://xml.weather.yahoo.com/forecastrss?p="+zip)

            #create an object that fetches responses/pages from the server
            opener = urllib2.build_opener()


            #tell object to go fetch response
            data = opener.open(request)

            #parse the info
            xmldoc = minidom.parse(data)

            titles = xmldoc.getElementsByTagName("titles")
            print titles[0].firstChild.nodeValue


            forecast = xmldoc.getElementsByTagName("yweather:forecast")
            c=""
            for i in forecast:
                c += i.attributes['day'].value + "(" + i.attributes['date'].value + ") <br />"
                c += "HIGH: " + i.attributes['high'] + ':::  ' + "LOW: " + i.attributes['low'].value
                c += "<img src=\"images/" + i.attributes['code'].value + '.png" width="30" />'
                c += '<br/>'
            self.responce.write(c)

        else:
            self.response.write(f.print_out())





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
        return self._head + self._form_open + self.create_inputs() + self._form_close + self._close

        #accept an array of dictionaries
        #use it to build





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
