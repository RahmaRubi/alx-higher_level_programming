#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    la = number % 10
else:
    la = number % -10
if la > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, la))
elif la == 0:
    print("Last digit of {} is {} and is 0".format(number, la))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, la))
