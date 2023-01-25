import random

computer = random.randint(1,3)

while True:
  player1 = input("rock, paper or scissors: ")
  if player1.lower() == "rock":
    player = 1
    break
  elif player1.lower() == "paper":
    player = 2
    break
  elif player1.lower() == "scissors":
    player = 3
    break
  else:
    print("\nThat wasn't an option :(\n\n")

if player == 1:
  if computer == 1:
    print("you tied!")
  elif computer == 2:
    print("the computer chose paper, you lose!")
  elif computer == 3:
    print("the computer chose scissors, you win!")
elif player == 2:
  if computer == 1:
    print("the computer chose rock, you win!")
  elif computer == 2:
    print("you tied!")
  elif computer == 3:
    print("the computer chose scissors, you lose!")
elif player == 3:
  if computer == 1:
    print("the computer chose rock, you lose!")
  elif computer == 2:
    print("the computer chose paper, you win!")
  elif computer == 3:
    print("you tied!")