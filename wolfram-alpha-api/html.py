__author__ = 'CarmineTrovato'

class HTML(object):
    def __init__(self):
        self._open = '''

<!DOCTYPE html>
<html>

<head>

<title>WolfSearchAPI</title>


<link rel="stylesheet" type="text/css" href={self.css}>
<link href={self._font} rel="stylesheet" type="text/css">
<link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">


</head>

<body>

<div class="container">

<div id="search">

<form action="/" method="GET">



<fieldset class="clearfix">
'''
    _content = '''

<input type="search" name="search" value="What are you looking for?" onBlur="if(this.value=='')this.value='What are you looking for?'" onFocus="if(this.value=='What are you looking for?')this.value='' ">
<input type="submit" value="Search" class="button">

</fieldset>

</form>

</div> <!-- end search -->

</div> <!-- end container -->
'''

    _close = '''

    </body>
</html>
'''
    def __init__(self):
        pass

    def print_out(self):
        return self._open + self._content + self._close



#This function overides the print function
    def print_out(self):
        return self._open + self._content + self._close

        #accept an array of dictionaries
        #use it to build

