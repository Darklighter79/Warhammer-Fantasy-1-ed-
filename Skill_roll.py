#skill test
import random

n = int(input("Enter your skill value: "))
a = int(input("Enter the number of actions: "))

crit_msg = ("Gods turned their attention away for a moment...",
            "You almost had it...almost",
            "Always look on the bright side of...warp",
            "Bring out yer dead!",
            "Do you have spare characted sheet ready?",
            "Dice do not like you I guess...",
            "Try to bargain with Game Master...",
            "Chaos gods unleashed their fury!")

for i in range(1, a+1):

    roll = random.randint(1, 100)

    if roll in range(96, 100) and n < roll:
        print(
            f"{i}. You rolled: {roll}. Critical failure! Test failed by: {roll - n}.That is {roll // n} of your skill. Voice of oracle: {random.sample(crit_msg, 1)}")
    elif roll in range(1, 6) and n > roll:
        print(
            f"{i}. You rolled: {roll}. Wow! Critical success! Test beaten by {n - roll}. That is {n // roll} of your "
            f"skill.")
    elif roll <= n:
        print(f"{i}. You rolled: {roll}. Sucess! Test beaten by {n - roll}. That is {n // roll} of your skill.")
    elif roll > n:
        print(f"{i}. You rolled: {roll}. Test failed by: {roll - n}. That is {roll // n} of your skill.")
