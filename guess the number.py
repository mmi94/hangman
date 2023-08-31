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
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty ():
  difficulty = input("Choose a difficulty, 'easy' or 'hard' ")
  if difficulty == 'easy':
    return EASY_LEVEL_TURNS
  else :
    return HARD_LEVEL_TURNS
def com_guess (guess, x, turn):
  if guess < x:
    print ("Too low.")
    return turn -1
  if guess > x:
    print ("Too high.")
    return turn - 1
  if guess == x:
    print ('Your guess is correct')
    return


print ('Welcome to the number guessing game. ')
print(logo)
print ("I am thinking of a number between 1 and 100")
x = random.randint(0, 100)
attempts = int (set_difficulty())
while attempts != 0:
  print (f'You have {attempts} attempts remaining to make a guess.')
  guess = int (input('Make a guess: '))
  attempts = com_guess(guess, x, attempts)
  if attempts == 0:
    print (f'The guess was {x}')