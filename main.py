#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)


EASY_ATTEMP = 10
HARD_ATTEMP = 5

def check(guess, number, attemp):
    if guess == number:
        print(f"You got it! The answer was {number}")
    elif guess < number:
        print("Too low.")
        print("Guess again.")
        return attemp -1
    else: 
        print("Too high.")
        print("Guess again.") 
        return attemp -1

def set_difficulty():
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficult == "easy":
        return EASY_ATTEMP
    else:
        return HARD_ATTEMP

def game():                                                                             
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    # print(f"The correct was {number}")

    attemp = set_difficulty()

    guess = 0

    while guess!= number:
        print(f"You have {attemp} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attemp = check(guess, number, attemp)

        if attemp == 0:
            print("You've run out of guesses, you lose. ")
            return 

game()