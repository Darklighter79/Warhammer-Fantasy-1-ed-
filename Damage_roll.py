import random

n = int(input("Input your strength value with all additional modifiers: "))

roll = random.randint(5, 6)

lst_num = [roll]

if roll == 6:
    while lst_num[-1] == 6:
        lst_num.append(random.randint(1, 6))
        print("Fury of Ulric! Additional damage!")

print(f'Your strength total: {n} and your roll is {lst_num}. Total {n + sum(lst_num)}.')
