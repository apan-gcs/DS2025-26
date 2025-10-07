"""
Ms. Pan
10/7/25
Int. Data Science II
Classwork: Dice Rolls Simulation

https://docs.google.com/document/d/1EiW_IjdvPY9T56EICANnwH9wPy4rJFm-Ys3QcfpRUgY/edit?tab=t.0#heading=h.md3whbfgdwnd
"""

import random
from time import sleep

# Exercise 1: 10 dice rolls
print("Simulation of 10 dice rolls:")

sum = 0
for i in range(10):
    roll = random.randint(1,6)
    sum += roll
    #print(roll)
    #sleep(0.5)
print(f"The sum is: {sum}")
print(f"The avg is: {sum/10}")

print("\n--------------\n")

# Exercise 2: 10,000 dice rolls
print("Simulation of 10,000 dice rolls:")

sum = 0
# This loop will start at 1 and end at 10000
# to help with counting current rolls
for i in range(1, 10001):
    roll = random.randint(1,6)
    sum += roll
    if i == 10:
        print(f"The average of 10 rolls is: {sum/10}")
    elif i == 100:
        print(f"The average of 100 rolls is: {sum/100}")
    elif i == 1000:
        print(f"The average of 1000 rolls is: {sum/1000}")
print(f"The average of 10000 rolls is: {sum/10000}")
