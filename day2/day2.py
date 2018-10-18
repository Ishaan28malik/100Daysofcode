import string
values = dict()
for position, letter in enumerate(string.ascii_lowercase):
    values[letter] = position + 1

alphabet = input("input the alphabet: ")

print (values[alphabet])

