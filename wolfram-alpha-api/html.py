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

<form action="javascript:void(0);" method="GET">

<fieldset class="clearfix">

<input type="search" name="search" value="What are you looking for?" onBlur="if(this.value=='')this.value='What are you looking for?'" onFocus="if(this.value=='What are you looking for?')this.value='' "> <!-- JS because of IE support; better: placeholder="What are you looking for?" -->
<input type="submit" value="Search" class="button">

</fieldset>

</form>

</div> <!-- end search -->

</div> <!-- end container -->
'''

        self._close = '''

    </body>
</html>
'''

