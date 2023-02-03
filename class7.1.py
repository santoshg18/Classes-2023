# positional arguments(arguments) and keyword arguments

def addition(abcd=12, y=10): # defaulted which you assign
    print('Value of x is', x)
    print('Value of y is', y)

# addition(12, 10)
# addition(y=12, x=10)
# addition(10, y=12)


# Dictionary
dict1 = {1: 'a', 2: 'b', 3: 'c'}


# def add(x, y, z):
#     print(x, y, z)
def add(*args, **kwargs):
    """Method Overloading"""
    # print(args, type(args))
    print(kwargs, type(kwargs))
    x = kwargs['x']
    y = kwargs['y']

# add()
add(x=1)
add(x=1, y=2)
add(x=1, y=2, z=3)
# add(1,2,3,4,5,6)


# git clone https://github.com/santoshg18/Classes-2023.git
# git ids - <> - group
# create your folder
# writing your code
# add, commit, push
# task - group