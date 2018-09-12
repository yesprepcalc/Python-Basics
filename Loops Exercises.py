#function that takes:
#a value x (to be used as diameter, base or side)
#a string shape (of either 'circle', 'triangle' or 'square')

def area(x, shape):
    import math
    possible = ['circle', 'triangle', 'square']
    #tests if given shape is not one we can find area of
    test = shape not in possible
    if test:
        return "error: invalid shape given"
    elif (shape is 'circle'):
        area = math.pi * (x/2)**2
        return area
    elif(shape is 'triangle'):
         height = x**2 - (x/2)**2
         area = x * height
         return(area)
    elif(shape is 'square'):
         area = x**2
         return(area)

possible = ['circle', 'triangle', 'square', 'rectangle']

for i in range(0,len(possible)):
    print(area(5,possible[i]))

#function that takes a list, start index and end index,
#applies quicksort and returns sorted list
    
def sum_of_squares(a, b):
    if len(a) != len(b):
        print("mismatched list dimensions")
        quit
    n = len(a)
    total = 0
    for i in range(0,n):
        total += (a[i]-b[i])**2
    return total

test1 = [3, 7, 1, 2, 0, 9]
test2 = [1, 1, 5, 4, 8, 3]
print(sum_of_squares(test1, test2))

test1.sort
test2.sort
print(sum_of_squares(test1, test2))
    
