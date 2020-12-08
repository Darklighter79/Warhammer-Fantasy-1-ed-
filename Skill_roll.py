#skill test.....
import random

n = int(input("Enter your skill value: "))
a = int(input("Enter the number of actions: "))

crit_msg = ["Gods are not on your side today",
            "Do you have spare character sheets ready?",
            "Maybe try to bargain with GM?",
            "Time for Destiny Point?",
            "I got a bad feeling about this..."]

for i in range(1, a+1):

    roll = random.randint(95, 100)

    if roll in range(96, 101) and n < roll:
        print(
            f"{i}. You rolled: {roll}. Critical failure! Test failed by: {roll - n}.That is {roll // n} of your skill."
            f"The voice of Oracle: {random.choice(crit_msg)}")
    elif roll in range(1, 6) and n > roll:
        print(
            f"{i}. You rolled: {roll}. Wow! Critical success! Test beaten by {n - roll}. That is {n // roll} of your "
            f"skill.")
    elif roll <= n:
        print(f"{i}. You rolled: {roll}. Sucess! Test beaten by {n - roll}. That is {n // roll} of your skill.")
    elif roll > n:
        print(f"{i}. You rolled: {roll}. Test failed by: {roll - n}. That is {roll // n} of your skill.")
