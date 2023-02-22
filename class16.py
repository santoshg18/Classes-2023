"""
pass, continue, break
OOPS concepts.
"""
# for n in range(10):
#     if n == 1:
#         continue
#     if n == 5:
#         break
#     print(n)

# for i in range(10):
#     for j in range(5):
#         if i == 5:
#             break
#         print(i, j)
#     if i == 7:
#         break


class A:
    """Class is a Blueprint of an object"""
    pass

# Object is an Instance of a class
a = A()


"""
Properties - Inheritence, Abstraction, classes, objects, Encapsulation, polymorphism
OOPS - Object Oriented Programming language.
"""

class Display:
    def _print(self, word):
        print(word)


# inhertience

class B(Display):
    def add(self, a, b):
        print(a + b)


b = B()
b._print('Santosh')
b.add(1,2)


# Class, Objects, Inheritence.

# Direct inheritence

class A:
    pass
class B:
    pass

class C(B):
    pass

# Multi level inheritence

class A:
    def f1(self):
        pass
class B(A):
    # f1 -> A
    # f2 -> B
    def f2(self):
        pass
class C(B):
    # f1, f2 functions available
    # f3 -> C
    def f3(self):
        pass

# Multiple inheritence

class A:
    pass
class B:
    pass
class C(A, B):
    pass