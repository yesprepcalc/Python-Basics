##Classes
#super useful, can create a "class" with
#functions ("methods") and variable "attributes")

#Ex: make a class of student attributes for each student
class Student(object):
    def __init__(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_major(self, major):
        self.major = major

anna = Student('anna')
anna.set_age(23)
anna.set_major('math')

print(anna.age)
print(anna.major)

##can make classes that inherit from other classes
class MasterStudent(Student):
    at_risk = 'this student is at risk of not graduating'

james = MasterStudent('james')
james.set_age(25)

james.age


###write a class called Circle that takes the radius
#and has two methods to compute the area and perimeter
import math

class Circle():
    
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        return (self.radius**2)*math.pi

    def perimeter(self):
        return self.radius*2*math.pi

test_Circle = Circle(5)

print(test_Circle.area())
print(test_Circle.perimeter())

