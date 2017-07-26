#!/usr/bin/python3
import random

computer_number = random.randint(0, 10)

while True:
    try:
        user_number = int(input("Please guess the number between 1 and 10: "))
        if (user_number == computer_number):
            break
        else:
            print('Sorry, that is not the number')

        if (user_number > 10):
            print('Please ensure you enter a number between 1 and 10')

    except ValueError:
        print('You didn\'t enter a number')

    except:
        print('An unknown error has occurred')

print("You guessed the right number!")