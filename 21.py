names = []

while True:
  cname = input("Enter name: ")
  if cname == "exit":
    break
  else:
    names.append(cname)

print(f"duplicates are {set([x for x in names if names.count(x) > 1])}")