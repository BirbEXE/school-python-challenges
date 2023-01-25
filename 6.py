import time

start, x = str(time.time()).split('.')

input("press enter when you think ten seconds has elapsed")

end, x = str(time.time()).split('.')

if (int(end) - int(start)) == 10:
  print("you got it, bang on!")
elif (int(end) - int(start)) <= 10:
  print("oops, you were too fast!")
  print(f"you pressed enter at {int(end) - int(start)} seconds")
elif (int(end) - int(start)) >= 10:
  print("too slow,")
  print(f"you pressed enter at {int(end) - int(start)} seconds")
