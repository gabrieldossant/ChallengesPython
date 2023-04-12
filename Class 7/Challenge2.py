from random import *

num = randint(0, 100)
control = 0
i = 0

while control == 0:
    i += 1
    x = int(input("Type your guess number:"))

    if num == x:
        print(f"Congratulations! Your attempts were {i}")
        control = 1
    elif num > x:
        print(f"The drawn number is greater than the number you guessed")
    else:
        print(f"The drawn number is smaller than the number you guessed")