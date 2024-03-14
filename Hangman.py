import random
from Hangman_words import word_list
from Hangman_art import stages, logo

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(f'Pssst, the solution is {chosen_word}.')
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  incorrect_guess = True
  for position in range(word_length):
    letter = chosen_word[position]
       
    if letter == guess:
      display[position] = letter
      incorrect_guess = False
      
  if incorrect_guess == True:
    lives -= 1

  print(f"{' '.join(display)}")
  print(stages[lives])
    
  if lives < 0:
    end_of_game = True
    print("You Lose.")
  elif "_" not in display:
    end_of_game = True
    print("You win.")