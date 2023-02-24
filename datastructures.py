class Stack:
    """Stack Datastructure
    Stack is a linear Data Structure that stores elements in a Last in First Out (LIFO) manner.
    |        |
    |        |
    |        |
    |________|

    Push - Add element to a stack
    Pop - Remove element to a stack
    isEmpty - Checks if stack is empty
    isFull - Checks if stack is full

    """
    def __init__(self, size): #4
        self.stack = [] # 0,1,2,3
        self.maxsize = size
        self.top = -1

    def push(self, x):
        if self.top == self.maxsize - 1:
            print('Stack is overflowed')
        else:
            self.x = x
            self.stack.append(x)
            self.top += 1

    def pop(self):
        if self.top == -1:
            print('Stack is underflow')
        else:
            self.stack.pop()
            self.top -= 1

    def isEmpty(self):
        print(self.top == -1)

    def isFull(self):
        print(self.top == self.maxsize-1)

    def peek(self):
        print(self.stack[-1])

    def display(self):
        for i in self.stack:
            print(i)


stackobj = Stack(100)
stackobj.push(10)
stackobj.push(20)
stackobj.push(30)
stackobj.push(40)
stackobj.display()
stackobj.isFull()
stackobj.pop()
stackobj.display()
print('*' * 10)
stackobj.pop()
stackobj.display()
print('*' * 10)
stackobj.pop()
stackobj.display()
print('*' * 10)
stackobj.pop()
stackobj.display()
stackobj.isEmpty()


