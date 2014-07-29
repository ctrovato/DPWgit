'''
Carmine Trovato
July 22, 2014
DPW Quiz Three
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = Submit()
        f._inputs = [{'type': 'text', 'placeholder': 'First Name', 'name': 'fname'},
                     {'type': 'text', 'placeholder': 'Middle Name', 'name': 'mname'},
                     {'type': 'text', 'placeholder': 'Last Name', 'name': 'lname'},
                     {'type': 'submit', 'name': 'submit', 'value': 'Enter'}]
        self.response.write(f.print_out())

class Display(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title>Carmine Trovato Quiz 4</title>
</head>
<body>"""
    _content = ''

    _close = """
</body>
</html>"""

class Submit(Display):
    _inputs = ''
    form_start = "<form method=GET action=""/>"
    form_end = "</form>"

    def __init__(self):
        Display.__init__(self)

    def inputinfo(self):
        _inputs=''
        for i in self._inputs:
            _inputs += '<input type="' + i['type'] + '" name="' + i['name'] + ' " '
            if 'placeholder' in i:
                _inputs += ' placeholder="' + i['placeholder']+ ' " '
            if 'value' in i:
                _inputs += ' value=" ' + i['value'] + ' " '
            _inputs += '/>'
        return _inputs

    def print_out(self):
        return self._head + self.form_start + self.inputinfo() + \
            self.form_end + self._close

app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
 ], debug=True)
