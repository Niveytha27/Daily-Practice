"""
For any random number from 0 to 10^12, generate its number name.
Note: Use Western Naming System [Ones, Tens, Hundreds, Thousands, Millions, Billions, Trillions] 
"""

# Imports
import random


# Core Logic
def namer(num):
    num_name = 'One'
    return num_name


# Driver
N = 10
L0, L1 = 0, 1e+12
numberlist = []
for _ in range(N):
    numberlist.append(random.randint(L0, L1))
for number in numberlist:
    print(f"Number : {number:15d} |  Number Name : {namer(number)}")