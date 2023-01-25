import random

numero = random.randint(1,100)
uncompleted = True
tries = 0

while uncompleted == True:
  guess = int(input("enter a number: "))
  if guess == numero:
    print("got it")
    break
  elif numero <= guess:
    print("too high")
    tries = tries + 1
  elif numero >= guess:
    print("too low")
    tries = tries + 1