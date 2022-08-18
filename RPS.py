import random

# Punteggio utente
userPoints = 0
# Punteggio computer
computerPoints = 0

# Possibili scelte dell'utente
user_choices = ["C", "F", "S", "c", "s", "f"]
# Possibili scelte del computer
computer_choices = ["C", "F", "S"]

while(True):

  # Mostro chi ha vinto
  if (userPoints == 3):
    print("\nCongratulazioni, hai vinto la partita :) ")
    break
  if (computerPoints == 3):
    print("\nPeccato, il computer ha vinto :( ")
    break

  # Messaggio di inizio del gioco
  print("\nCarta, Forbice, Sasso...")

  # Scelta dell'utente
  inp = input("Scegli tra [C]arta, [F]orbice o [S]asso: ")
  if (inp == 'C' or inp == 'c'):
    userChoice = 'Carta'
  if (inp == 'S' or inp == 's'):
    userChoice = 'Sasso'
  if (inp == 'F' or inp == 'f'):
    userChoice = 'Forbice'

  # Se l'utente fa una scelta non valida
  if not inp in user_choices:
    print("Perfavore inserisci una scelta valida...")
    continue

  # Mostro cosa ha scelto l'utente
  print("Hai scelto: " + userChoice)

  # Scelta del computer
  cmp = random.choice(computer_choices)
  if (cmp == 'C' or cmp == 'c'):
    computerChoice = 'Carta'
  if (cmp == 'S' or cmp == 's'):
    computerChoice = 'Sasso'
  if (cmp == 'F' or cmp == 'f'):
    computerChoice = 'Forbice'
  
  # Mostro cosa ha scelto il computer
  print("Il computer ha scelto: " + computerChoice)

  if cmp == inp.upper():
    print("Pareggio! ")

  elif cmp == 'S' and inp.upper() == 'F':
    print("Sasso batte forbici, Ho vinto! ")
    computerPoints+=1
    continue

  elif cmp == 'F' and inp.upper() == 'C':
    print("Forbici batte carta, Ho vinto! ")
    computerPoints+=1
    continue

  elif cmp == 'C' and inp.upper() == 'S':
    print("Carta batte sasso, Ho vinto! ")
    computerPoints+=1
    continue

  else:
    print("Hai vinto!")
    userPoints+=1