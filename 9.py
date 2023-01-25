import random

while True:
  suit = random.randint(1,4)
  card = random.randint(1,13)

  if suit == 1:
    suit = "Spades"
  elif suit == 2:
    suit = "Diamonds"
  elif suit == 3:
    suit = "Hearts"
  elif suit == 4:
    suit = "Clubs"

  if card == 1:
    card = "Ace"
  elif card == 2:
    card = "2"
  elif card == 3:
    card = "3"
  elif card == 4:
    card = "4"
  elif card == 5:
    card = "5"
  elif card == 6:
    card = "6"
  elif card == 7:
    card = "7"
  elif card == 8:
    card = "8"
  elif card == 9:
    card = "9"
  elif card == 10:
    card = "10"
  elif card == 11:
    card = "Jack"
  elif card == 12:
    card = "Queen"
  elif card == 13:
    card = "King"

  print(f"your card was the {card} of {suit}")
  input("\nPress enter to generate another card\n\n")