str = input("enter a sentence to count: ")
words = str.split()
count = 0

for word in words:
  count = count + 1

print(count)