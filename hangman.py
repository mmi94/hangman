#Step 2
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code

display = []
lives = 6
for i in chosen_word:
  display.append("_") 

end_of_game = False
while not end_of_game:
    clear()
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print ('You have already guessed this letter')
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display [i] = guess
    if guess not in chosen_word :
        lives -= 1
        print (stages[lives])
        if lives == 0:
            end_of_game = True
            print ('you\'re out of lives, GAME OVER ')
    if '_' not in display:
        end_of_game = True
        print ("You win")
    print (' '.join(display))