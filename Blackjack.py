############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
import random
'''
l = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
q1 = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
computer = []
user = []

def deal ():
#get 2 random cards 
  x = random.choice(l)
  user.append(x) 
  x = random.choice(l)
  user.append(x)
  x = random.choice(l)
  computer.append(x)
  x = random.choice(l)
  computer.append(x)

if q1 == 'y':
  deal()
cont = True
while cont :
  x = random.choice(l)
  computer.append(x)
  x = random.choice(l)
  computer.append(x)
  if 11 in computer and 10 in computer:
    print ("computer win")
  elif 11 in user and 10 in user :
    print ("You win ")
  else:
    computer_score = sum(computer)
    user_score = sum(user)
    if user_score > 22 :
      if 11 in user:
        if user_score - 10 > 21:
          print( "you lose")
        else:
          q2 = input(" do you want to get another card? ")
          if q2 == 'n':
            if computer_score < 17:
              x = random.choice(l)
              computer.append(x)
              if computer_score > 21:
                print ("you win")
              else:
                if computer_score > user_score:
                  print ("computer win")
                elif computer_score < user_score:
                  print ("you win")
                else :
                  print ("Draw")
          if q2 == "y":
            cont = true
      else:
        print( "you lose")

'''
#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.


#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice( cards)
def calculate_score (list):
  if sum (list) == 21 and len (list) == 2:
    return 0
  elif sum (list) >21 and 11 in list:
    return sum (list) - 10
  return sum (list)

def compare(s1, s2):
  if s2 == 0:
    print( 'computer win')
  elif s1 == 0:
    print("you win")
  elif s2 < s1 < 21:
    print ("you win")
  elif s1 < s2 < 21:
    print ("computer win")
  elif 21 < s1 < s2:
    print ("computer win")
  elif 21 < s2 < s1:
    print ("you win")
  elif s1 == s2:
    print ("Draw")
    
  
user_cards = []
computer_cards = []
end_of_game = False

for i in range (2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
restat = True
while restart:
  while not end_of_game:
    computer_score = calculate_score (computer_cards)
    user_score = calculate_score (user_cards)
    print (f"your cards {user_cards}, your score is {user_score}")
    print (f"computer first card is {computer_cards[0]}")
    
    if computer_score == 0 or user_score == 0 or user_score > 21:
      end_of_game = True
    else:
        draw = input ('Do you want to draw another card yes or no? ')
        if draw == "yes":
          user_cards.append(deal_card())
          calculate_score(user_cards)
        if draw == "no":
          end_of_game = True
    while computer_score < 17 and computer_score != 0:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
      if computer_score == 0:
        print ("computer win")
      else:
        compare(user_score, computer_score)
    
  new_game = input ("do you want to restart the game yes or no? ")
  if new_game == "yes":
    clear()
    restart = True
  else :
    restart = False
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

