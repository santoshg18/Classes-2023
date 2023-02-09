"""
Generators, Loop Statements, Class method, static method.
Author: Santosh
Date: 09-Feb-2023
"""


# Generator function

def function_normal():
    # executes something
    print('I am a normal function')
    return 10

def function_generator():
    yield 10

def func_range_gen(end):
    """yield the current state of that function is sent back."""
    out = 0 # Initializing the value of out to Zero
    while out < end:
        yield out
        out = out + 1 # incrementing the value of out

#
# print(f'User defined Range function: {func_range_gen(10)}')
# print(f'Pre defined Range function: {range(10)}')
# print(function_normal())
#
# for i in func_range_gen(10):
#     print(i)


# loops statements
# for, while
# for a in 'Python':
#     print(a)
# a = 0
# while a < 1:
#     print('This is unlimited loop')
#     a = a + 1


def manideep_range_function(start, end, step):
    for i in range(start, end, step):
        print(i)
# manideep_range_function(1,11,2)


l = [1, 2, 3]
# print(len(l))

def user_defined_length_function(_list):
    c = 0
    for i in _list:
        c = c + 1
    return c

# print(user_defined_length_function(l))


# Classes

class PythonClass:
    class_name = 'Python Class 2023'
    def __init__(self, num):
        self.number = num # Instance variables
        self.names = ['a', 'b', 'c']

    def number_of_students(self):
        """Instance Method"""
        return self.number
    @classmethod
    def change_class_name(cls, name):
        cls.class_name = name
    @staticmethod
    def tutor():
        print('Santosh')

def tutor():
    print('Santosh')
p = PythonClass(6)
# print(p.number_of_students())
q = PythonClass(2)
# print(q.number_of_students())
# print(PythonClass.class_name)
# print(p.class_name)
# print(q.class_name)

# PythonClass.change_class_name('Class Python 2023')
# print(PythonClass.class_name)
# print(p.class_name, q.class_name)

PythonClass.tutor()
q.tutor()