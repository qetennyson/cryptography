message = 'three can keep a secret, if two of them are dead'
translateda = ''
translatedi = ''
i = len(message) - 1
a = len(message)

# The while loops are valuable here because you are reversing the string.
# Using a for loop starts from the beginning of a string, and while you could do
# something to make it work, it wouldn't be as clear.

while i >= 0:
    print(translatedi)
    translatedi += message[i]
    print(translatedi)
    print(i)
    i -= 1
    print(i)

while a >= 0:
    print(translateda)
    translateda += message[a]
    print(translatedi)
    print(a)
    a -= 1
    print(a)

my_dog = "fido"
correct = len(my_dog) - 1
too_long = len(my_dog)
print(correct)
print(too_long)
