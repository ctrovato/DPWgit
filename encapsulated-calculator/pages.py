'''
Carmine Trovato
July 15th 2014
DPW 1407 Encapsulated Calculator
'''



class Television(object):
    def __init__(self):
        self.__television = ""
        self.__price = 0
        self.__sound = 0
        self.__bluray = 0
        self.__warranty = 0
        self.__total = 0
        self.__open = '''

<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
        <link href='http://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>

        <title>Encapsulated Calculator</title>
    </head>
    <body>
        '''
        self.header = '''
        <header>
            <h1>Top-Rated Television & Package Deals</h1>

        </header>
        '''
        self.__paragraphs = '''
        <div id="links">
            <h2 id="firstH2">TV Models</h2>
            <a href="?television=samsung">Samsung 48" LED HDTV</a>
            <a href="?television=sony">Sony BRAVIA 52" LED HDTV</a>
            <a href="?television=lg">LG 48" LED HDTV</a>
            <a href="?television=vizio">VIZIO M-Series 42" LED HDTV</a>
            <a href="?television=insignia">Insignia 42" LED HDTV</a>
       </div>
       <div id="paragraphs">
            <h2>TV Package Prices</h2>
            <h4 id = brand>{self.television}</h4>
            <p id = price>TV Price: ${self.price}</p>
            <p id = sound>Surround-Sound: ${self.sound}</p>
            <p id = bluray>BluRay: ${self.bluray}</p>
            <p id = warranty>Warranty: ${self.warranty}</p>
            <p id = total>Total: ${self.total}</p>
        </div>
        '''
        self.__close = '''
    </body>
</html>
        '''
        self.__all = self.__open + self.header + self.__paragraphs + self.__close

    @property
    def television(self):
        return self.__television

    @television.setter
    def television(self, new_television):
        self.__television = new_television

    @property
    def bluray(self):
        return self.__bluray

    @bluray.setter
    def bluray(self, new_bluray):
        self.__bluray = new_bluray

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new_sound):
        self.__sound = new_sound

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, new_total):
        if new_total < 800:
            self.__total = str(new_total)
        else:
            self.__total = new_total


    def print_out(self):
        self.update()
        return self.__all

    def update(self):
        self.__all = self.__all.format(**locals())