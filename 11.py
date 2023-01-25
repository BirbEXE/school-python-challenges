while True:
  player1 = input("what gate? AND, OR, or XOR: ")
  if player1.lower() == "or":
    player = 1
    break
  elif player1.lower() == "and":
    player = 2
    break
  elif player1.lower() == "xor":
    player = 3
    break
  else:
    print("\nThat wasn't an option :(\n\n")

first = int(input("enter first input (1/0): "))
second = int(input("enter second input (1/0): "))

if player == 1:
  if first == 0:
    if second == 0:
      print("output = 0")
      exit()
    elif second == 1:
      print("output = 1")
      exit()
  elif first == 1:
    print("output = 1")
    exit()
elif player == 2:
  if first + second == 2:
    print("output = 1")
    exit()
  else:
    print("output = 0")
    exit()
elif player == 3:
  if second + first == 1:
    print("output = 1")
  else:
    print("output = 0")