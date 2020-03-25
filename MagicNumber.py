from random import *

magic_number = randint(0, 10)
user_number = input('Enter an integer from 0 to 10: ')
user_number = int(user_number)
if magic_number == user_number:
    print('Congratulations, You Have Won')
else:
    print('Its Okay, Try Again')
