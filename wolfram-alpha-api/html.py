__author__ = 'CarmineTrovato'

class HTML (object):

    def __init__(self):
        pass

    _open = '''

<!DOCTYPE html>
<html>

<head>

<title>WolfSearchAPI</title>


<link rel="stylesheet" href="css/style.css" type="text/css" />

<link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">


</head>

'''
    _content = '''

<body>

<div class="container">

<div id="search">


<h3 class="logo">Wolfram-Alpha API</h3>
<form action="/" method="GET">



<fieldset class="clearfix">



<input type="search" name='search' class='search' value="Ask me anything..." onBlur="if(this.value=='')this.value='Ask me anything...'" onFocus="if(this.value=='Ask me anything...')this.value='' ">

<input type="submit" value="Find" id="button">

</fieldset>

</form>

<h3 class="resultsHeader">{self.formattedSearch}</h3>
<div class="results">
    {self.answer}
</div>

</div> <!-- end search -->

</div> <!-- end container -->
'''

    _close = '''

    </body>
</html>
'''

    search = ''
    answer = ''

    @property
    def formattedSearch(self):
        if self.search == '':
            return ''
        else:
            return ' Results For "' + self.search + '''"
            <script>
                var u = new SpeechSynthesisUtterance(" ''' + self.answer + ''' ");
                speechSynthesis.speak(u);
            </script>
            '''


#This function overides the print function

    def print_out(self):
        return self._open + self._content.decode('utf-8').format(**locals()) + self._close

        #accept an array of dictionaries
        #use it to build

