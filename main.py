import random
from words import word_list
from hangman_art import logo
from hangman_art import stages

print(logo)

word = random.choice(word_list)
word_length = len(word)
display = []
lives = len(stages)
game_over = False
for _ in range(word_length):
  display.append("_")


print(display)
while not game_over :
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print("You already guess this letter")
  
  for position in range(word_length):
    letter = word[position]
    if guess == letter:
      display[position] = letter
      print(display)
      
  if guess not in word:
    lives -=1
    print(stages[lives-1])
    print(display)
    if lives == 0:
      print(f"You are out of lives, the word was : {word}")
      game_over = True

  if "_" not in display:
    print(f"You win, the word is: {word}")
    game_over = True
   
  


