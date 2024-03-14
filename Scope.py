################### Scope ####################

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
ANSWER = random.choice(range(1,101))

def game():
    return int(input("Make a guess: "))
    
def game_easy():
    games_finished = False
    chance = 10
    while chance >= 0 and not games_finished:

        guess = game()
        chance -= 1
        if chance == 0:
            print("Game over, no attempts left")
            break
        elif guess < ANSWER:
            print("Too low")
            print(f"You have {chance} attempts remaining to guess the number")
        elif guess > ANSWER:
            print("Too high")
            print(f"You have {chance} attempts remaining to guess the number")
        elif guess == ANSWER:
            print("You're correct")
            games_finished = True
        
def game_hard():
    games_finished = False
    chance = 5
    while chance >= 0 and not games_finished:

        guess = game()
        chance -= 1
        if chance == 0:
            print("Game over, no attempts left")
            break
        elif guess < ANSWER:
            print("Too low")
            print(f"You have {chance} attempts remaining to guess the number")
        elif guess > ANSWER:
            print("Too high")
            print(f"You have {chance} attempts remaining to guess the number")
        elif guess == ANSWER:
            print("You're correct")
            games_finished = True

if DIFFICULTY == 'easy':
    game_easy()
else:
    game_hard()


