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

#user input
width = raw_input('Enter Width')
height = raw_input('Enter Height')

#calc_area for integers width and height
calc_area(int(width), int(height))


#function count_down each time it runs will  count down number of bottles of beer
def count_down(count):
    for i in range(count):
#prints out the count each time
        print str(count) + " Bottles on the wall. " + str(count) + " Bottles of beer." \
                                             " Take one down and pass it around. Now you have " + str(count-1) + " bottles of beer on the wall."
        count -= 1  #count down number of bottles of beer by one
count_down(10)
