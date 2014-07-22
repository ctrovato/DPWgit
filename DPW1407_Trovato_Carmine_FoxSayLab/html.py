__author__ = 'CarmineTrovato'

class Html(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.main_title} | {self.title}</title>
        <link rel="stylesheet" type="text/css" href={self.css}>
        <link href={self._font} rel="stylesheet" type="text/css">
        <script src="js/modernizr.2.5.3.min.js"></script>


    </head>
    <header>
        <h1>What does the Fox Say? Lab</h1>
        <nav>
            <ul>
                <li><a href="?animal=fox">The Fox</a></li>
                <li><a href="?animal=rabbit">The Rabbit</a></li>
                <li><a href="?animal=wolf">The Wolf</a></li>
            </ul>
        </nav>
    </header>
    <body id="{self._body_id}">
        '''
        self._content = '''
        </div>
        <div id="info">
            <h2>{self.animal} Information</h2>
            <p><span>Phylum:</span> {self._phylum}</p>
            <p><span>Class:</span> {self._class_}</p>
            <p><span>Order:</span> {self._order}</p>
            <p><span>Family:</span> {self._family}</p>
            <p><span>Genus:</span> {self._genus}</p>
            <p><span>Avg Life Span:</span> {self._avg_lifespan}</p>
            <p><span>Habitat:</span> {self._habitat}</p>
            <p><span>Geo Location:</span> {self._geo_location}</p>
            <p><span>Sound:</span> {self.sound}</p>
        </div>
        <div id ="image">
            <h2 id="animal_image">Animal: {self.animal}</h2>
            <figure>
                <img id ="the_fox" src="{self._fox}" alt="">
                <img id ="the_image" src="{self._url}" alt="{self.animal}">
            </figure>
        </div>
        '''

        self._close = '''

    </body>
</html>
        '''
