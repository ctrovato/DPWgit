
import webapp2
from views import Page   # you can use * for wild card



class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        #Send in content we need
        p.content = "Sign the form below:"
        p.css = "css/styles.css"
        # p.title = "Welcome"
        #print out the content tpo the branch
        self.response.write(p.print_out())





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
