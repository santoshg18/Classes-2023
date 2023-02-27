"""
Method overriding.. Inheritance
BTWN
Method overloading.. Polymorphism

Abstraction and Encapsulation
"""


class School:
    def name(self, n, sort=True):
        print('I am in school')


class Class(School):
    def name(self, m, sort=True):
        print('I am in class')

    def display(self, *args):
        print('Displaying...')
        print(args)


# c = Class()
# c.name()


# Method Overloading

def display(arg1):
    print('Displaying...')
    print(arg1)

def display(arg1, arg2):
    print('Displaying...')
    print(arg1, arg2)

def display(arg1, arg2, arg3):
    print('Displaying...')
    print(arg1, arg2, arg3)


def display(*args):
    print('Displaying...')
    print(args)

# display(1)
# display(1,2)
# display(1,2,3)
# display()


# Abstraction = Hiding some internal functionalities
# Encapsulation

"""
Both are Related to each other.
"""
class School:
    def __init__(self):
        """Dunder method - magic method which will be called whenever a class is created.
        Is is a constructor."""
        self.name = "St John's"


    def about(self):
        self.addr = "Hyderabad, India"
        self.pincode = 500092
        self.contact = "+91-99999-00000"
        print(self.addr, self.pincode, self.contact)

    def subjects(self):
        self.no_of_subjects = 6
        self.list_of_subjects = ['a','b','c','d','e','f']
        print(self.no_of_subjects, self.list_of_subjects)


# s = School()
# print(s.name)
# s.subjects()

# 1
x = 1
y = 2
# print(x+y)
# print(x-y)

# 2
def add(x, y):
    print(x + y)
def substract(x,y):
    print(x -y)

# add(1, 2)
# add(2, 3)
# substract(5, 1)
# substract(10, 3)


# 3

class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print('Adding the numbers')
        print(self.x + self.y)

    def substract(self):
        print('Substracting...')
        print(self.x - self.y)


# m = Math(10, 5)
# m.add()
# m.substract()


class Math2(Math):
    def multiply(self):
        print('Multiplying..')
        print(self.x * self.y)


m2 = Math2(5, 3)
m2.multiply()
