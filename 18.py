def drawstars(x, y):
  statement = ""
  for num in range(x):
    statement = statement + " "
  for thingy in range(y):
    statement = statement + "*"
  return(statement)

print(f"{drawstars(2,3)}\n{drawstars(2,3)}\n{drawstars(3,1)}\n{drawstars(2,3)}\n{drawstars(0,7)}\n{drawstars(2,1)}{drawstars(1,1)}\n{drawstars(1,2)}{drawstars(1,2)}")