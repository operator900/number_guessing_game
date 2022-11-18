#Create a game that makes the computer pick a number between 1 - 100.
#Easy level: User gets 10 attempts to try to guess the number.
#Hard level: User only gets 5 attempts to guess the number.

import random as rdm
import number_guessing_functions as ngg

print(ngg.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = rdm.randint(1, 101)

print(ngg.game(difficulty=difficulty, pc_num = random_number))