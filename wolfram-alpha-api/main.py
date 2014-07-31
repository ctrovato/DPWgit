'''
Carmine Trovato
July 23th 2014
DPW1407 Wolfram API
'''


# from google.appengine.api import urlfetch
# urlfetch.set_default_fetch_deadline(45)
import webapp2
from urllib import quote
from html import HTML
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        q = HTML()

        if self.request.GET:
            search = self.request.GET['search']

            wolframModel = WolframModel()
            answer = wolframModel.search(search)
            q.answer = answer
            q.search = search

        self.response.write(q.print_out())


class ResultsDataObject(object):

    def __init__(self):
        self.search = ""
        self.queryresult = ""
        self.title = ""
        self.plaintext = ""
        self.subpod = ""
        self.img = ""
        self._font = "http://fonts.googleapis.com/css?family=Open+Sans 'rel='stylesheet"


class SearchView(object):
    def __init__(self):
        self.__wolfram = ""
        self.queryResults = []

    @property
    def wolfram(self):
        pass




class WolframModel(object):

    def __init__(self):
        self.url = "http://api.wolframalpha.com/v2/query?appid=GGEKR4-H8KK93WL94&input="

    def search(self, query):

        safeQuery = quote(query, safe="%/:=&?~#+!$,;'@()*[]")

        #creates a request to send to server
        request = urllib2.Request(self.url + safeQuery)
        opener = urllib2.build_opener()
        xmldoc = opener.open(request)
        xmlobject = minidom.parse(xmldoc)
        pods = xmlobject.getElementsByTagName("pod")

        for pod in pods:
            if pod.attributes.has_key('primary'):
                answer = pod.getElementsByTagName("plaintext")[0].firstChild.nodeValue
                return answer

        return ''

        # searchResult = pods[1].getElementsByTagName("subpod")[0].getElementsByTagName("plaintext")[0].firstChild.nodeValue
        #
        # dataObject = ResultsDataObject();
        #
        # dataObject.plaintext = pods[1].getElementsByTagName("subpod")[0].getElementsByTagName("plaintext")[0].firstChild.nodeValue
        # dataObject.img = pods[1].getElementsByTagName("subpod")[0].getElementsByTagName("img")[0].firstChild.nodeValue
        #
        # dataObject.primary = pods[1].getElementsByTagName("subpod")[0].getElementsByTagName("primary")[0].firstChild.nodeValue
        #
        # return dataObject


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)