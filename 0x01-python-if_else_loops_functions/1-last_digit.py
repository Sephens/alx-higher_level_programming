#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if( digit == 0):
    print(f"The last digit of {number} is {digit} and is 0")
elif( digit > 5):
    print(f"The last digit of {number} is {digit} and is greater than 5")
elif( digit > 0 and digit < 6):
    print(f"The last digit of {number} is {digit} and is greater than 0 and less than 6")
