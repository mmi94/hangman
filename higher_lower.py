from game_data import data
import art
#from replit import clear
import random
A = random.choice(data)
B = random.choice(data)
def higher_lower (A, B):
  print (art.logo)
  L1 = []
  for key in A:
    L1.append(A[key])
  print (f"Compare A: {L1[0]}, a {L1[2]}, from {L1[3]}.")
  L2 = []
  for key in B:
    L2.append(B[key])
  print (art.vs)
  print (f"Against B: {L2[0]}, a {L2[2]}, from {L2[3]}.")
  a = input("Who has more followers? Type 'A' or 'B': ").upper ()
  if L1[1] > L2 [1]:
    return [a, 'A', A]
  else:
    return [a, 'B', B]

end_game =False
score = 0
answer = higher_lower (A, B)
print (answer[0] , answer[1], answer[2])
while not end_game:
  if answer[0] == answer[1]:
    score += 1
    print (f"You're right! Current score: {score}")
    answer = higher_lower (answer[2], random.choice(data))
    
  else :
    end_game = True
    print (f"Sorry, that's wrong. Final score: {score}")



#print (f': ')
#print ("Who has more followers? Type 'A' or 'B': ")
#clear()