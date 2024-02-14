import random
import os

def clear():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')

starting = input("Do you want to play a game of Blackjack? Type 'y' or 'n: ").lower()
if starting == "y":
    clear()

your_card = []
user_score = 0
comp_card = []
comp_score = 0

def cards_init():
    global user_score, comp_score

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_card.extend(random.sample(cards,2))
    comp_card.append(random.choice(cards))
    user_score = sum(your_card)
    comp_score = sum(comp_card)
    if user_score == 21:
        user_score = 0
    if 11 in your_card and user_score > 21:
        your_card.remove(11)
        your_card.append(1)

def cards_add_user():
    global user_score

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_card.append(random.choice(cards))
    user_score = sum(your_card)
    if 11 in your_card and user_score > 21:
        your_card.remove(11)
        your_card.append(1)

def cards_add_comp():
    global comp_score

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    comp_card.append(random.choice(cards))
    comp_score = sum(comp_card)
    if 11 in comp_card and comp_score > 21:
        your_card.remove(11)
        your_card.append(1)
    if comp_score == 21 and len(comp_card):
        comp_score = 0

def blackjack():
    print(f"Your cards: {your_card}, current score: {user_score}")
    print(f"Computer's first card: {comp_card[0]}")

    while True:
        if user_score == 0:
            break
        continues = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if continues == "y":
            cards_add_user()
            print(f"Your cards: {your_card}, current score: {user_score}")
            if user_score > 21:
                break
        elif continues == "n":
            while comp_score < 17 and comp_score !=0:
                cards_add_comp()
                if comp_score == 0 or comp_score > 21:
                    break
            break

cards_init()
blackjack()
print(f"Your final hand: {your_card}, final score: {user_score}")
print(f"Computer's final hand: {comp_card}, final score: {comp_score}")
if user_score > 21:
    print("You went over. You lose")
elif comp_score > 21:
    print("Opponent went over. You win")
elif user_score > comp_score:
    print("You win")
elif user_score == comp_score:
    print("Draw")
elif comp_score == 0:
    print("Lose, opponent has Blackjack")
elif user_score == 0:
    print("Win with a Blackjack")
else:
    print("You lose")