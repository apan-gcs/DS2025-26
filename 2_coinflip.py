"""
Ms. Pan
9/12/25
Intensive Data Science 2
Classwork #2 - Math in Python

Exploring math module and calculating coin flip probabilities.
https://docs.google.com/document/d/14y7IGrPb1hzgQmtO7UTWF_aL-vcZsjNYtyctnepuxHw/edit?tab=t.0#heading=h.45qpnqgbtodw
"""

import math

#print(math.pi)
#print(math.sin(math.pi/6))
#print(math.exp(1))
#print(math.sqrt(100))
#print()

print("Coin Flip Probability Calculator")

# Ask the user for n
n = int(input("How many coins do you want to flip?  "))

# Ask the user for k
k = int(input("How many heads do you want?  "))

# Probability = nCr / 2^n
probability = math.comb(n, k) / 2**n

# Convert the probability to % and round to the tenths
percentage = round(probability * 100, 1)
print("The probablity is: " + str(percentage) + "%")
