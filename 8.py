from datetime import datetime

dob, mob, yob = [int(x) for x in input("Enter your age (DD/MM/YYYY): ").split('/')]
bdy = datetime(yob, mob, dob)

daystotal, x, y = str(datetime.now() - bdy).split(' ')

if int(daystotal) >= 6570:
  print("you are old enough to vote")
else:
  print("go back to school")