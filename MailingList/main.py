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
    content = '''Hello There'''
    form_content = '''
        <form method="GET">
        <div id= "wrapper">
            <h4>Sign Up</h4>
            <input type="text" placeholder="First Name" name= "fname" />
            <br/>
            <input type="text" placeholder="Last Name" name= "lname"  />
            <br/>
            <input type="text" placeholder="Email Address" name= "email"  />
            <br/>
            <input type="password" placeholder="Enter Password" name= "pass"  />
            <br/>
            <input type="text" placeholder="Re-Type Password" name= "repass"  />
            <br/>


        <div id ="dropbox" class="float_left clear">
        <h4>Newsletter: <br> Would You like to receive Newsletters via Email</h4>
        <select name = "marketing">
            <option> Select One</option>
            <option value = "week" name = "week">Yes, Weekly</option>
            <option value = "month" name = "month">Yes, Monthly</option>
            <option value = "annually" name= "none">Yes, Annually</option>
            <option value = "none" name= "none">No, Thank You</option>
        </select>

        <h4>How Would you describe yourself (check all that may apply)</h4>
            <input type="checkbox"  name= "artistic" value ="Artistic">Artistic<br/>
            <input type="checkbox"  name= "athletic" value ="Athletic">Athletic<br/>
            <input type="checkbox"  name= "music" value ="Music">Music Snob<br/>
            <input type="checkbox"  name= "food" value ="Foodie">Foodie

            </div>

            <input type="submit" value="submit info" />
        <div>
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
