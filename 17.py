mod1 = int(input("enter module one grade: "))
mod2 = int(input("enter module two grade: "))

if mod1 >= 80:
  grade1 = "A"
elif mod1 >= 70:
  grade1 = "B"
elif mod1 >= 60:
  grade1 = "C"
elif mod1 >= 50:
  grade1 = "D"
elif mod1 >= 40:
  grade1 = "F"

if mod2 >= 80:
  grade2 = "A"
elif mod2 >= 70:
  grade2 = "B"
elif mod2 >= 60:
  grade2 = "C"
elif mod2 >= 50:
  grade2 = "D"
elif mod2 >= 40:
  grade2 = "F"

if (mod1+mod2) >= 160:
  ASlvl = "A"
elif (mod1+mod2) >= 140:
  ASlvl = "B"
elif (mod1+mod2) >= 120:
  ASlvl = "C"
elif (mod1+mod2) >= 100:
  ASlvl = "D"
elif (mod1+mod2) >= 80:
  ASlvl = "F"

print("Module 1: {}".format(grade1))
print("Module 2: " + str(grade2))
print(f"AS level: {ASlvl}")