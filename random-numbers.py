"""Example of using random numbers."""
import random

x = random.random()  # random floating point number between 0 and 1
print(x)

y = random.randint(1, 20)  # random integer between 1 and 20
print(y)

lottery = [1, 20, 31, 5, 19, 23, 59]
random.shuffle(lottery)
print(lottery)

class1 = ["James", "Charmian", "Linda", "Steven"]
luckyWinner = random.sample(class1, 1)
print(luckyWinner)
