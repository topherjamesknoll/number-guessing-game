# Project 1 - Number Guessing Game

import random

secret_number = random.randint(1, 20)

def start_game():
    tries = 0
    print("Welcome to the Number Guessing Game!!!")
    while True:
        try:
            guess = int(input("Guess a number between 1 and 20 > "))
            if guess > 20:
                raise ValueError
            elif guess < 1:
                raise ValueError
        except ValueError:
            print("Sorry that is not a valid number.")
        else:
            if guess > secret_number:
                print("It's lower.")
            elif guess < secret_number:
                print("It's higher.")
            else:
                print("Got it! You won in", tries, "tries!")
                break
            tries += 1
    print("Thanks for playing!!!")

start_game()