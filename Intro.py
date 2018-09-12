import os
import math
os.getcwd()
#os.chdir()

##variables
a = 5
b = 7.34
c = "dog "

type(a)
type(b)
type(c)

##operations
a + b - 4 
(b*a)/3
a**2

#can use math module for
print(math.log(2))
print(math.e**3)
print(math.log(math.e**5)) #will return what?

##logical comparisons
3 > 4
a < b
a >= b

##logical operations
print((a > 3) and (b > a)) #only true if both are true, o/w false
print((a > 3) or (b > a)) #only false if both are false, o/w true
print(not (3 > 4))

##input/output
age = eval(input("How old are you? "))
print("Ok, so you are", age, "years old.", sep = " ")

print("when I see a pup, I say hi", c, sep = " ")
print("when I see three I say hi", 3*c, sep = " ")

##basic data structures
#lists
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple', 'black', 'white']
len(colors)
type(colors)
print(colors)

print(colors[3])
print(colors[-1])
print(colors[2:5])

colors.append('pink') #adds item to list
colors.pop() #removes last item
sorted(colors) #returns new sorted list
colors.sort() #sorts the list and saves it as colors

#strings
h = "hello"
print(h)

output = 'processing file %i out of %i with name %s, took %f seconds' % (17, 25, 'dog.jpg', 12.45)
print(output)

#dictionaries (map keys to values)
fam = {'mom':'donna', 'dad':'rick', 'brother':'david', 'sister':'amanda'}
print(fam['brother'])

##exercises: volume and area of circle/sphere
##find difference of given number and 17,
#if greater than 17 return twice the absolute difference
##test whether number is within 100 of 1000 or 2000
##find GCD b/t two numbers using Euclid algorithm
