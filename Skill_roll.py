import random

n = int(input("Enter your skill value: "))
a = int(input("Enter the number of actions: "))

for roll in range (0, a):

    roll = random.randint(1, 100)

    if roll in range(96, 100) and n < roll and roll in range(0, a):
        print(
            f"You rolled: {roll}. Critical failure! Test failed by: {roll - n}.That is {roll // n} of your skill")
    elif roll in range(1, 4) and n > roll:
        print(f"You rolled: {roll}. Wow! Critical success! Test beaten by {n - roll}. That is {n // roll} of your skill")
    elif roll <= n:
        print(f"You rolled: {roll}. Sucess! Test beaten by {n - roll}. That is {n // roll} of your skill")
    elif roll > n:
        print(f"You rolled: {roll}. Test failed by: {roll - n}. That is {roll // n} of your skill")














