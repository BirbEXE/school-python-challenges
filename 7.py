import time

start, x = str(time.time()).split('.')

print("please type the alphabet below! remember, no spaces.\n")
alphabeta = input()

end, x = str(time.time()).split('.')

if alphabeta.lower() == "abcdefghijklmnopqrstuvwxyz":
  print("\nnot bad, for a toddler.")
  print(f"you took {int(end) - int(start)} seconds.")
else:
  print("\npathetic.")
  print(f"you just spent {int(end) - int(start)} seconds of your life writing the alphabet, and you still got it wrong.")
  print("I almost feel sorry for you.")