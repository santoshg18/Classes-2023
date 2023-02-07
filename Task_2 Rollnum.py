# class



class roll_num:

    def __init__(self, name, rn):
        print('student is created - init')
        self.name = name
        self.rn = rn


    def student_id(self):
        print('This is student ID.')

dev1 = roll_num('mani', '3')
dev2 = roll_num('python', '4')
dev3 = roll_num('django', '5')


print(dev1.name, dev1.rn)
print(dev2.name, dev2.rn)
print(dev3.name, dev3.rn)