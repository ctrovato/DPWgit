'''
Carmine Trovato
July 23th 2014
DPW1407 Wolfram API
'''



import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        q = QueryPage()
        q.inputs =[{'type': 'search', 'placeholder':'What are you looking for?', 'name': 'search'}]

        if self.request.GET:

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


class SearchView(object):
    def __init__(self):
        self.__wolfram = ""
        self.queryResults = []

    @property
    def wolfram(self):
        pass



class Page(object):

    _head = """<!DOCTYPE HTML>
<head>
    <title>WolfRamAlpha API</title>
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



class QueryPage():
    _form_open = "<form method=\"GET\" action=""  />"
    _form_close = "</form>"
    additional_view = ""


    def __init__(self):
        #invoke constructor in superclass
        QueryPage.__init__(self)

    @property
    def input(self):
        pass

    @input.setter
    def input(self, i):
        self.__input = i

    def create_inputs(self):
        tot_inputs = ''
        for i in self.__input:

        return input



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

        searchResult = pods[1].getElementsByTagName("subpod")[0].getElementsByTagName("plaintext")[0].firstChild.nodeValue

        dataObject = ResultsDataObject();

        dataObject.plaintext = pods[1].getElementsByTagName("subpod")[0].getElementsByTagName("plaintext")[0].firstChild.nodeValue
        dataObject.img = pods[1].getElementsByTagName("subpod")[0].getElementsByTagName("img")[0].firstChild.nodeValue


        return dataObject


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)