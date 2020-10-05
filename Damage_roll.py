import random

n = int(input("Input your strength value with all additional modifiers: "))

roll = random.randint(1, 6)

lst_num = [roll]

if roll == 6:
    while lst_num[-1] == 6:
        lst_num.append(random.randint(1, 6))
    print(f'Fury of Ulric! Additional damage!Your strength total: {n} and your roll is {lst_num}. Total {n + sum(lst_num)}.')
else:
    print(f'Your strength total: {n} and your roll is {lst_num}. Total {n + sum(lst_num)}.')
