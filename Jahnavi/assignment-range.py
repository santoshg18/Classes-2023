import string
for i in range(0,10):
    print(i)

print("---------------")

for i in range(0,10 + 1):
    print(i)

print("---------------")

for i in range(0,10 + 1, 2):
    print(i)

print("---------------")

for letters in string.ascii_uppercase:
    print(letters, end = " ")

print("\n","---------------")

for letter in string.ascii_lowercase:
    print(letter, end = " ")