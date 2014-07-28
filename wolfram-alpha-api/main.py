'''
Carmine Trovato
July 23th 2014
DPW1407 Wolfram API
'''



import webapp2
import urllib2
from xml.dom import minidom
from html import HTML

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # q = QueryPage()
        # q.inputs =[{'type' : 'search', 'placeholder':'What are you looking for?', 'name': 'search'}]
        # if there is stuff in the url, do stuff
        # if self.request.GET:

        wolframModel = wolframModel()
        wolframModel.search('pi')


        # self.response.write(q.print_out())




class ResultsDataObject(object):

    def __init__(self):
        self.queryresult = ""
        self.title = ""
        self.plaintext = ""
        self.subpod = ""
        self.img = ""


    def parse(self):
        xmldoc = minidom.parse(self.data)
        forecast = xmldoc.getElementsByTagName("pod")

        self.__dos = []
        for item in forecast:
            do = WolframModel()
            do.title = item.attributes['title'].value
            do.scanner = item.attributes['scanner'].value
            do.id = item.attributes['id'].value
            do.position = item.attributes['position'].value
            do.error = item.attributes['error'].value
            do.numbersubpod = item.attributes['numbersubpod'].value
            #this adds the finished data objects into the array
            self.__dos.append(do)






class SearchView(object):
    def __init__(self):
        self.__wolfram = ""
        self.queryResults = []

    @property
    def wolfram(self):
        pass

    @queryResults.setter
    def queryResults(self, arr):
        self.__queryResults = arr
        self.create_display()

    def create_display(self):
        for do in self.__dos:
            self.content += "Day:" + do.day
            self.content += " (" + do.date + ')'
            self.content +=" High: " + do.high + " Low: " + do.low
            self.content += "<img src=\"images/" + do.code + '.png" />'
            self.content += "<br />"
        print self.content



class QueryPage():
    __inputs = []
    _form_open = "<form method=\"GET\" action=""  />"
    _form_close = "</form>"
    additional_view = ""


    def __init__(self):
        #invoke constructor in superclass
        QueryPage.__init__(self)

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




class WolframModel(object):

    def __init__(self):
        self.url = "http://api.wolframalpha.com/v2/query?appid=GGEKR4-H8KK93WL94&input=pi"

    def results(self, query):
        #creates a request to send to server
        request = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        xmldoc = opener.open(request)
        xmlobject = minidom.parse(xmldoc)
        pods = xmlobject.getElementsByTagName("pod")

        result = pods[1].getElementsByTagName("subpod")[0].getElementsByTagName("plaintext")[0].firstChild.nodeValue

        print result


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)