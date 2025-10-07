"""
Ms. Pan
9/19/25
Intensive Data Science 2
Classwork #4 - Random Numbers

Exploring random module and simulating a coin flip.
https://docs.google.com/document/d/18zz15FVh6TT7K_vNl5VAwDcxYKIGL3hFbnE4-GZbSog/
"""

import random

#random.seed(42)               # Change seed for different results
#print(random.random())        # Random float between 0 and 1
#print(random.randint(1, 10))  # int between 1 and 10 (inclusive)

# Ask the user how many dollars to bet

money = int(input(""))

print(f"You bet {money} dollars. Now flipping a coin...")

# Coin flip, 1 = heads, 0 = tails
coin = random.randint(0, 1)

# Double or nothing...
if coin == 1:
    print(f"Heads. You have {money*2} dollars!")
else:
    print("Tails. You have no money now.")
