import random

# Punteggio utente
userPoints = 0
# Punteggio computer
computerPoints = 0

# Possibili scelte dell'utente
user_choices = ["P", "S", "R", "p", "s", "r"]
userChoice = ''
# Possibili scelte del computer
computer_choices = ["P", "S", "R"]
computerChoice = ''

while(True):

  # Mostro chi ha vinto
  if (userPoints == 3):
    print("\nCongratulations, you won the game :) ")
    break
  if (computerPoints == 3):
    print("\nToo bad, the computer won :( ")
    break

  # Messaggio di inizio del gioco
  print("\nRock, Paper, Scissor...")

  # Scelta dell'utente
  inp = input("Choose between [R]ock, [P]aper or [S]cissor: ")
  if (inp == 'P' or inp == 'p'):
    userChoice = 'Paper'
  if (inp == 'R' or inp == 'r'):
    userChoice = 'Rock'
  if (inp == 'S' or inp == 's'):
    userChoice = 'Scissor'

  # Se l'utente fa una scelta non valida
  if not inp in user_choices:
    print("Please enter a valid choice ...")
    continue

  # Mostro cosa ha scelto l'utente
  print("You chose: " + userChoice)

  # Scelta del computer
  cmp = random.choice(computer_choices)
  if (cmp == 'P' or cmp == 'p'):
    computerChoice = 'Paper'
  if (cmp == 'R' or cmp == 'r'):
    computerChoice = 'Rock'
  if (cmp == 'S' or cmp == 's'):
    computerChoice = 'Scissor'
  
  # Mostro cosa ha scelto il computer
  print("Computer chose: " + computerChoice)

  if cmp == inp.upper():
    print("Tie! ")

  elif cmp == 'R' and inp.upper() == 'S':
    print("Rock beats scissors, I won! ")
    computerPoints+=1
    continue

  elif cmp == 'S' and inp.upper() == 'P':
    print("Scissors beats paper, I won! ")
    computerPoints+=1
    continue

  elif cmp == 'P' and inp.upper() == 'R':
    print("Paper beats rock, I won! ")
    computerPoints+=1
    continue

  else:
    print("You won!")
    userPoints+=1
