'''
Carmine Trovato
Date: 07/10/14
Quiz 1
'''

#function calc_area(w,h) takes the width and height
def calc_area(w,h):
    if w == h:
        print "This is a square of: " + str(w * h) + " square feet, because the width and height are the same."

    else:
        print "This is a rectangle of: " + str(w * h) + " square feet"
        return w * h

calc_area(20,10)
calc_area(4,10)

#function count_down each time it runs will  count down number of bottles of beer
def count_down(count):
