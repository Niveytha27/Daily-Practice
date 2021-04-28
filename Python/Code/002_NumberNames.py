"""
For any random number from 0 to 10^12, generate its number name.
Note: Use Western Naming System [Ones, Tens, Hundreds, Thousands, Millions, Billions, Trillions] 
"""

# Imports
import random

num_dict1 = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six', 7: 'Seven',
             8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
             14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen'}
num_dict2 = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy',
             8: 'Eighty', 9: 'Ninety'}
ten_power = {1: 'Billion', 2: 'Million', 3: 'Thousand', 4: 'Hundred'}


# Core Logic
def name_gen1(n):
    if n == 0:
        name = ''
    x = divmod(n, 100)
    if x[0] == 0 and x[1] != 0:
        y = divmod(x[1], 10)
        name = name_gen2(x[1], y)
    elif x[0] != 0:
        if x[1] == 0:
            name = num_dict1[x[0]]
            y = divmod(x[1], 10)
            name += ' ' + ten_power[4]
        else:
            name = num_dict1[x[0]]
            y = divmod(x[1], 10)
            name += ' ' + ten_power[4] + ' and ' + name_gen2(x[1], y)
    return name


def name_gen2(x,y):
    n_name = ''
    if y[0] == 0 and y[1] != 0:
        n_name = num_dict1[y[1]]
    elif y[0] == 1:
        n_name = num_dict1[x]
    elif y[0] != 0 and y[1] == 0:
        n_name = num_dict2[y[0]]
    elif y[0] != 0 and y[1] != 0:
        n_name = num_dict2[y[0]] + ' ' + num_dict1[y[1]]
    return n_name


def split_num(num):
    if num == 0:
        name = num_dict1[num]
    elif len(str(num)) <= 3:
        name = name_gen1(num)
    elif 3 <= len(str(num)) <= 6:
        num1, num2 = divmod(num, 1000)
        num_name1 = name_gen1(num1)
        num_name2 = name_gen1(num2)
        name = f"{num_name1} {get_power_name(num1,3)} {num_name2}"
    elif 6 <= len(str(num)) <= 9:
        n, num3 = divmod(num, 1000)
        num1, num2 = divmod(n, 1000)
        num_name1 = name_gen1(num1)
        num_name2 = name_gen1(num2)
        num_name3 = name_gen1(num3)
        name = f"{num_name1} {get_power_name(num1,2)} {num_name2} {get_power_name(num2,3)} {num_name3}"
    elif 9 <= len(str(num)) <= 12:
        n, num4 = divmod(num, 1000)
        n1, num3 = divmod(n, 1000)
        num1, num2 = divmod(n1, 1000)
        num_name1 = name_gen1(num1)
        num_name2 = name_gen1(num2)
        num_name3 = name_gen1(num3)
        num_name4 = name_gen1(num4)
        name = f"{num_name1} {get_power_name(num1,1)} {num_name2} " \
               f"{get_power_name(num2,2)} {num_name3} {get_power_name(num3,3)} {num_name4}"
    return name


def get_power_name(num, e):
    if num == 0:
        power_name = ''
    elif num != 0  and e == 1:
        power_name = ten_power[1]
    elif num != 0  and e == 2:
        power_name = ten_power[2]
    elif num != 0  and e == 3:
        power_name = ten_power[3]
    return power_name


# Driver
N = 10
L0, L1 = 0, 1e+12
numberlist = []
for _ in range(N):
    numberlist.append(random.randint(L0, L1))
for number in numberlist:
    print(f"Number : {number:15d} |  Number Name : {split_num(number)}")