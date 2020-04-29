# Project 1 - Number Guessing Game

SECRET_NUMBER = 76

def start_game():

    tries = 0
    print("Welcome to the Number Guessing Game!!!")
    while True:
        try:
            guess = input("Guess a number between 1 and 100 > ")
            if guess > 100:
                raise NameError
            if guess < 1:
                raise NameError
        except NameError:
            print("Sorry that is not a valid number.")
        else:
            if guess > SECRET_NUMBER:
                guess = input("It's lower. Try again > ")
            elif guess < SECRET_NUMBER:
                guess = input("It's higher. Try again > ")
            else:
                print("Got it! You won in {} tries!").format(tries)
                break
            tries += 1
    print("Thanks for playing!!!")

start_game()