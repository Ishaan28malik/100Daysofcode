string = input("input string :")

def slice(string):
    length_string = len(string)
    first_length = round(length_string / 2)
    first_half = string[0:first_length].lower()
    second_half = string[first_length:].upper()
    return first_half + second_half

slice()