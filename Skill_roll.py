#skill test
import random

n = int(input("Enter your skill value: "))
a = int(input("Enter the number of actions: "))

crit_msg = ("Wsadź łeb pod wóz", "Po co przyjechałeś?", "Mogłeś się dać na eksperymenty w Nuln", "Pogrom! Wrogowie podejrzewają, że jesteś jedynie dywersją", "Losuj nową postać",
            "Nie grasz przez rok", "Mike, daj końmi do tyłu", "Od dziś jesteś na liście kapłanej Shyalli jako cel do atakowania obok wyznawców Nugrla")

for i in range(1, a+1):

    roll = random.randint(1, 100)

    if roll in range(96, 100) and n < roll:
        print(
            f"{i}. You rolled: {roll}. Critical failure! Test failed by: {roll - n}.That is {roll // n} of your skill. Głos wyroczni: {random.sample(crit_msg, 1)}")
    elif roll in range(1, 6) and n > roll:
        print(
            f"{i}. You rolled: {roll}. Wow! Critical success! Test beaten by {n - roll}. That is {n // roll} of your "
            f"skill.")
    elif roll <= n:
        print(f"{i}. You rolled: {roll}. Sucess! Test beaten by {n - roll}. That is {n // roll} of your skill.")
    elif roll > n:
        print(f"{i}. You rolled: {roll}. Test failed by: {roll - n}. That is {roll // n} of your skill.")
