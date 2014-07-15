'''
 Carmine Trovato
 July 14th 2014
 Lab  1: Simple Form
'''




import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #YOU CANT USE self.response or self.request
        #both attributes of your MainHandler class.
        p = Page()  #creating an instance  "p" of class Page


        if self.request.GET:
            p.content = "First Name:" + self.request.GET['fname']
            p.content += "<br />Last Name:" + self.request.GET['lname']
            p.content += "<br />Email:" + self.request.GET['email']
            p.content += "<br />Password:" + self.request.GET['pass']
            p.content += "<br />Re-Password:" + self.request.GET['repass']
            p.content += "<br /> Newsletter:" + self.request.GET['marketing']

            p.content += "<br />Describe Yourself:"

            if self.request.GET.has_key('artistic'):
                p.content += self.request.GET['artistic'] + ', '

            if self.request.GET.has_key('athletic'):
                p.content += self.request.GET['athletic'] + ', '

            if self.request.GET.has_key('artistic'):
                p.content += self.request.GET['artistic'] + ', '

            if self.request.GET.has_key('music'):
                p.content += self.request.GET['music'] + ', '

            if self.request.GET.has_key('food'):
                p.content += self.request.GET['food'] + ', '

            self.response.write(p.print_out_page())

        else:
            self.response.write(p.print_out_form())

class Page(object):
    header = '''<!DOCTYPE>
<html>
    <head>
        <link rel="stylesheet" href="style/style.css" type="text/css" />
        <title>LAB: Simple Form</title>
    </head>
    <body>
    '''
    content = '''Hello '''
    form_content = '''
        <form method="GET">
            <h3 class"header">Sign Up</h3>
            <input type="text" class="formfield"  placeholder="First Name" name= "fname" />
            <br/>
            <input type="text" class="formfield" placeholder="Last Name" name= "lname"  />
            <br/>
            <input type="text" class="formfield" placeholder="Email Address" name= "email"  />
            <br/>
            <input type="password" class="formfield" placeholder="Enter Password" name= "pass"  />
            <br/>
            <input type="text" class="formfield" placeholder="Re-Enter Password" name= "repass"  />
            <br/>

        <div id ="dropbox" class="float_left clear">
        <h4>Newsletter: <br> via Email</h4>
        <select name = "marketing">
            <option> Select One</option>
            <option value = "week" name = "week">Yes, Weekly</option>
            <option value = "month" name = "month">Yes, Monthly</option>
            <option value = "annually" name= "none">Yes, Annually</option>
            <option value = "none" name= "none">No, Thank You</option>
        </select>

        <h4>Describe yourself </br>(check all that may apply)</h4>
            <input type="checkbox"  name= "artistic" value ="Artistic">Artistic<br/>
            <input type="checkbox"  name= "athletic" value ="Athletic">Athletic<br/>
            <input type="checkbox"  name= "music" value ="Music">Music Snob<br/>
            <input type="checkbox"  name= "food" value ="Foodie">Foodie

            </div>
            <br/>
            <input type="submit" class= "buttonStyle" value="Submit" />
        </div>

        </form>
    '''
    closer = '''
    </body>
</html>
    '''


    def __init__(self):
        pass

    def print_out_page(self):
        return self.header + self.content + self.closer

    def print_out_form(self):
        return self.header + self.form_content + self.closer




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
