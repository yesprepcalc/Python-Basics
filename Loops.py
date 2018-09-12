import os
import math

##if statements
#can use logical operators, 'is' or 'in'
x = eval(input("enter a number"))
if (x > 50):
    print("that's a big number")
elif (x > 1000):
    print("that's a really big number")
else:
    print("that's not that big")

##while loops
i = 0
while(i < 10):
    print("the counter is at %i" % (i))
    i += 1
    if (i ==8):
        break

##for loops
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(0,len(colors)):
    print("my favorite color is %s" % (colors[i]))

##functions
def distance(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

print(distance(1,3,6,8))

##modules
import demo
print(demo.test())
print(demo.test2())

#######################################

###make a function called area that takes arguments x and shape
#where x is either the base of an equilateral triangle,
#diameter of a circle or side of a square
#and shape is either 'triangle', 'square' or 'circle'
#the function should return the area of this shape

#use a for loop with your function to find the area
#of a triangle, square and circle where x = 5
#also try to find the area of a rectangle with this loop

##make a function called sum_of_squares that takes two lists of equal length
#and returns the sum of the squared difference between each element of the list

##bonus: save these functions as separate .py files and
#write a main file that import them
######################################
