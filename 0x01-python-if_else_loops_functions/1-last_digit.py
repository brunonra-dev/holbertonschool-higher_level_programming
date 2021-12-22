#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = ((number * -1) % 10) * -1
if last > 5:
    str = 'Last digit of {} is {} and is greater than 5'
elif last == 0:
    str = 'Last digit of {} is {} and is 0'
elif last < 6 and last != 0:
    str = 'Last digit of {} is {} and is less than 6 and not 0'
print(str.format(number, last))
