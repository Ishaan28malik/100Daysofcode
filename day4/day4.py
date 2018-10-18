def password():
       import random
       import string
       upper = (string.ascii_uppercase)
       lower = (string.ascii_lowercase)
       number = (string.digits)
       symbols = (string.punctuation)
       Light=  lower + number
       Middle= upper + lower + number
       Strong= upper + lower + number + symbols
       quess= input('How Secure must have light/middle/strong ?: ')
       x= input('How many characters would you like in your password?: ')
       if quess == 'light':
            light= "".join(random.sample(Light, x))
            print (light)
       elif quess == 'middle':
            middle= "".join(random.sample(Middle, x))
            print (middle)
       elif quess == 'strong':
            strong = "".join(random.sample(Strong, x))
            print (strong)
       else:
            print ('Invalid syntax, try again')
            password()

if __name__ == "__main__":
 password()