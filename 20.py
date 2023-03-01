a = 0
b = 1
listy = []
listy.append(a)
listy.append(b)

pos = int(input("which position in the sequence do you want to see? "))

while len(listy) < pos + 1:
  c = a + b
  a = b
  b = c
  listy.append(c)

print(listy[pos])