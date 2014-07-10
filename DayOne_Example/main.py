'''
# Carmine Trovato
# 07/08/2014
# Day One Example
'''



first_name = "Carmine"
last_name = "Trovato"

year_born = 1987
age = 2014 - year_born


print "I am " + str(age) + " years old"


age = raw_input("Type your age:")
print "You are " + age + " years old"




budget = 200
shoe_price = 60
won_lottery = True
if shoe_price <= budget:
    print  "buy the shoes"
elif won_lottery:
    print "buy the shoes"
else:
    print "buy the shoes"

print " I am done with code"



#FUNCTIONS

def calc_area(w,h):
    a = w * h
    return a
area = calc_area(50,60)
print str(area) + "ddfgdfg"




# LOOPS & ARRAYS
for i in  range(0,6,2):
    print i

students = ['Studnicky','Julian','Seth','Jordan','Danny','Carmine','Manny']
students.append('Alan')

for s in students:
    print s


#DICTIONARTIES
obj = {"name" : "Jordan", "age" : 20, "occupation" : "students"}
print obj ["name"][2]

big_string = '''
    Welcome to the python class, {user_name},
    you are going to do so well in this class
'''

user_name = "Seth"
print big_string.format(**locals())


tuple = (23, 56)


# strings that occupy more than one line