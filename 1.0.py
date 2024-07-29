from random import *

number = randint(1, 100) # We generate any number from 1 to 100
print("Добро пожаловать в числовую угадайку")

def is_invalid(arg):
    arg = int(input())
    if arg.isdigit():
        if 1 <= arg <= 100:
            return True
        else:
            return False
    else:
        return False
    
arg = input()
print(is_invalid(arg))