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
def name_gen1(n, e):
    if n == 0:
        name = ' '
    x = divmod(n, 100)
    if x[0] == 0 and x[1] != 0:
        y = divmod(x[1], 10)
        name = name_gen2(x[1], y)
    elif x[0] != 0:
        if x[1] == 0:
            name = num_dict1[x[0]]
            y = divmod(x[1], 10)
            name += ' ' + ten_power[4] + ' and ' + name_gen2(x[1], y)
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


def namer(num):
    num_name = ""
    if num == 0:
        num_name = num_dict1[num]
    elif 1 <= num < 1e+3:
        num = int(str(num))
        num_name = name_gen1(num, 4)
    elif 1e+3 <= num < 1e+6:
        num1, num2 = int(str(num)[:-3]), int(str(num)[-3:])
        num_name = name_gen1(num1, 3) + ' ' + ten_power[3] + ', ' + name_gen1(num2, 4)
    elif 1e+6 <= num < 1e+9:
        num1, num2, num3 = int(str(num)[:-6]), int(str(num)[-6:-3]), int(str(num)[-3:])
        num_name = name_gen1(num1, 2) + ' ' + ten_power[2] + ', ' + \
            name_gen1(num2, 3) + ' ' + ten_power[3] + ', ' + name_gen1(num3, 4)
    elif 1e+9 <= num < 1e+12:
        num1, num2, num3, num4 = int(str(num)[:-9]), int(str(num)[-9:-6]), \
                                 int(str(num)[-6:-3]), int(str(num)[-3:])
        num_name = name_gen1(num1, 1) + ' ' + ten_power[1] + ', ' + name_gen1(num2, 2) + ' ' + ten_power[2] + ', ' + \
            name_gen1(num3, 3) + ' ' + ten_power[3] + ', ' + name_gen1(num4, 4)
    return num_name


# Driver
N = 10
L0, L1 = 0, 1e+12
numberlist = []
for _ in range(N):
    numberlist.append(random.randint(L0, L1))
for number in numberlist:
    print(f"Number : {number:15d} |  Number Name : {namer(number)}")